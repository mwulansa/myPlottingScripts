import ROOT, os, sys
import myPlotFunc

iteration = "applyFF"
ver = "v1"

#dRLoose, inVer = v6
#dRTight, inVer = v8

inVer = "v8"

altVer = "v10"
inDataVer = "v10" 
altDataVer = "v10" 

DR = "DR2"
FFver = "dRTight"
# FFver = "dRLoose"
massTCP = "m30"

path = '/Users/muti/Documents/Analysis/studyCleanedTaus/'+iteration+"_"+ver
isExist = os.path.exists(path)

if not isExist:
	os.makedirs(path)
	print("Folder created, outputs in", path)

if isExist:
	print("Outputs in", path)

FfSource = '/Users/muti/Documents/Analysis/studyCleanedTaus/Ff_v'+FFver+'/F_F_'+DR+'_Ff_TauPt.txt'
print("FFfile = ", FfSource)

SAMPLES = ['Diboson','WJetsToLNu','DYJetsToLL','DYJetsToLL_M-4to50','TTJets']


# ROOT.gStyle.SetOptStat(111010)

out = ROOT.TFile(path+"/appliedFf_"+DR+"_v"+FFver+".root",'recreate')

c1 = ROOT.TCanvas("c1","c1",850, 850)
c1.cd()	
c1.SetGridx()
c1.Print(path+"/"+iteration+"_"+DR+"_"+FFver+".pdf[")

if FFver == "dRTight":
	f = ROOT.TFile("h_hMuTau_SR_highMET_lowMt_dRcut_TauPtMass_AlteredID_"+altVer+".root")
if FFver == "dRLoose":
	f = ROOT.TFile("h_hMuTau_SR_highMET_lowMt_dRcut_TauPtMass_loosedR_AlteredID_"+altVer+".root")
fd1 = ROOT.TFile("h_debugMuTau_HighHT_Data_Altered_SingleMuon_"+altDataVer+".root")
fd2 = ROOT.TFile("h_debugMuTau_HighHT_Data_Altered_JetHT_"+altDataVer+".root")

if FFver == "dRLoose":
	d1 = fd1.Get("hMuTau_SR_highMET_lowMt_dRcut_TauPtMass_loosedR")	
	d2 = fd2.Get("hMuTau_SR_highMET_lowMt_dRcut_TauPtMass_loosedR")
if FFver == "dRTight":
	d1 = fd1.Get("hMuTau_SR_highMET_lowMt_dRcut_TauPtMass")	
	d2 = fd2.Get("hMuTau_SR_highMET_lowMt_dRcut_TauPtMass")

data = d1.Clone("data")
data.Add(d2)
data.Sumw2()

bkgStack = ROOT.THStack("bkgStack","hMuTau_SR_highMET_lowMt_dRcut_TauPtMass;Tau P_{T} (GeV);M_{#mu#tau} (GeV)")

hists = {}

for sample in SAMPLES:
	if FFver == "dRLoose":
		h = f.Get(sample+"_hMuTau_SR_highMET_lowMt_dRcut_TauPtMass_loosedR")
	if FFver == "dRTight":
		h = f.Get(sample+"_hMuTau_SR_highMET_lowMt_dRcut_TauPtMass")
	bkgStack.Add(h)
	hists[sample] = h

htotal = hists['Diboson'].Clone("htotal")
for sample in SAMPLES:
	if sample != 'Diboson':
		htotal.Add(hists[sample])

hdiff = data.Clone("hdiff")
hdiff.Sumw2()

hdiff.Add(htotal, -1)

data.Rebin2D(20,5)
hdiff.Rebin2D(20,5)

nbinx = hdiff.GetNbinsX()
nbiny = hdiff.GetNbinsY()

FfFile = open(FfSource, 'rt')
Ff = [[float(token) for token in line.split()] for line in FfFile.readlines()]
print(Ff)

hdiffNew = hdiff.Clone("hdiffNew")
hdiffNew.Sumw2()

newVALUES = []
oldVALUES = []

for r in range(0, 13):
    newVALUES.append([0 for c in range(0, nbiny)])
    oldVALUES.append([0 for c in range(0, nbiny)])

for i in range(13):
	for j in range(nbiny):
		val = hdiff.GetBinContent(i+1, j+1)
		newVal = val*Ff[i][1]
		hdiffNew.SetBinContent(i+1, j+1, newVal)
		
		oldVALUES[i][j] = val
		newVALUES[i][j] = newVal
	
print("New Values")
print(newVALUES)
print("Old Values")
print(oldVALUES)

projx = hdiff.ProjectionX()
projy = hdiff.ProjectionY()

projxNew = hdiffNew.ProjectionX()
projyNew = hdiffNew.ProjectionY()

c1.SetLogz()
c1.SetRightMargin(0.15)
hdiff.SetStats(0)
hdiff.SetMinimum(0.01)
hdiff.Draw("colz")
hdiff.GetXaxis().SetRangeUser(0,260)
hdiff.SetTitle("Application Region, Data - MC_{nonQCD}")
c1.SaveAs(path+"/"+iteration+"_"+DR+"_AR_Data-MC_{nonQCD}_"+FFver+".png")
c1.Print(path+"/"+iteration+"_"+DR+"_"+FFver+".pdf")
c1.Clear()

projx = myPlotFunc.plotStyle(projx, 20, 4, 0, xtitle = "TauPt (GeV)",  fillStyle = 1001)
projx.Draw()
projx.GetXaxis().SetRangeUser(0,260)
c1.Print(path+"/"+iteration+"_"+DR+"_"+FFver+".pdf")
c1.Clear()

c1.SetLogy()
projy = myPlotFunc.plotStyle(projy, 5, 4, 0, xtitle = "M_{vis.} (GeV)",  fillStyle = 1001)
projy.Draw()
c1.Print(path+"/"+iteration+"_"+DR+"_"+FFver+".pdf")
c1.Clear()

print("data", data.Integral())
print("htotal", htotal.Integral())
print("hdiff", hdiffNew.Integral())

#------newHist
c1.SetLogz()
c1.SetLogy(0)
hdiffNew.SetStats(0)
hdiffNew.SetMinimum(0.01)
hdiffNew.Draw("colz")
hdiffNew.GetXaxis().SetRangeUser(0,260)
hdiffNew.SetTitle("Predicted QCD Background in SR")
c1.SaveAs(path+"/"+iteration+"_"+DR+"_Predicted_"+FFver+".png")
c1.Print(path+"/"+iteration+"_"+DR+"_"+FFver+".pdf")
c1.Clear()

projxNew = myPlotFunc.plotStyle(projxNew, 20, 4, 0, xtitle = "TauPt (GeV)",  fillStyle = 1001)
projxNew.Draw()
projxNew.GetXaxis().SetRangeUser(0,260)
c1.Print(path+"/"+iteration+"_"+DR+"_"+FFver+".pdf")
c1.Clear()

out.cd()
projyNew.Write("appliedFF_"+DR)
out.Close()

lg = ROOT.TLegend(0.3,0.7,0.83,0.88)
lg.SetLineWidth(0)
lg.AddEntry(projyNew, "Predicted QCD in SR = "+str(int(projyNew.Integral())), "l")

c1.SetLogy()
projyNew.SetMinimum(1)
projyNew.SetTitle("Predicted QCD Background in SR - Y Projection")
projyNew = myPlotFunc.plotStyle(projyNew, 5, 4, 0, xtitle = "M_{vis.} (GeV)",  fillStyle = 1001)
projyNew.Draw("hist e")
lg.Draw("same")
c1.SaveAs(path+"/"+iteration+"_"+DR+"_Predicted_YProj_"+FFver+".png")
c1.Print(path+"/"+iteration+"_"+DR+"_"+FFver+".pdf")
c1.Clear()

#-----overlay with MC

projyNew = myPlotFunc.plotStyle(projyNew, 5, lineColour = 12, xtitle = "M_{vis.} (GeV)")

# def makeBkgStack(rootFile, SAMPLE, histo, xtitle = "x", ytitle = "y"):

SAMPLES = ['Diboson','WJetsToLNu','DYJetsToLL','DYJetsToLL_M-4to50','TTJets','QCD']

rootFile = "h_hMuTau_SR_dRcut_highMET_lowMt_Nominal_"+inVer+".root"
histo = "hMuTau_SR_dRcut_highMET_lowMt"
xtitle = "M_{vis.} (GeV)"
ytitle = "Events / 5 GeV"

f = ROOT.TFile(rootFile)
tmpStack = ROOT.THStack("tmpStack",histo+";"+xtitle+";"+ytitle)

histMass = {}
integralSF = {}

for sample in SAMPLES:
	h = f.Get(sample+"_"+histo)
	h.Rebin(5)
	tmpStack.Add(h)
	integralSF[sample] = h.Integral()
	histMass[sample] = h

htot_nQCD = histMass['Diboson'].Clone("htot_nQCD")

for sample in SAMPLES[1:-1]:
	htot_nQCD.Add(histMass[sample])

htot_nQCD = myPlotFunc.plotStyle(htot_nQCD, 5, lineColour = 12, xtitle = "M_{vis.} (GeV)")

projyNew.Add(htot_nQCD)

errMass = projyNew.Clone("err")

errMass.SetFillColor(12);
errMass.SetFillStyle(3244);

s1 = f.Get("TCP_Ntuple_"+massTCP+"_HT-100to400_hMuTau_SR_dRcut_highMET_lowMt")
s2 = f.Get("TCP_Ntuple_"+massTCP+"_HT-400toInf_hMuTau_SR_dRcut_highMET_lowMt")

sig = s1.Clone("TCP")
sig.Sumw2()
sig.Add(s2)
sig.Rebin(5)

sig = myPlotFunc.plotStyle(sig, 5, 4, 4, fillStyle = 3334)

lgSF = ROOT.TLegend(0.3,0.7,0.83,0.88)
lgSF.SetLineWidth(0)
lgSF.SetNColumns(2)
lgSF.AddEntry(histMass['QCD'], "MC_{QCD} - "+str(int(integralSF['QCD'])), "f");
lgSF.AddEntry(histMass['TTJets'], "TTJets - "+str(int(integralSF['TTJets'])), "f");
lgSF.AddEntry(histMass['DYJetsToLL'], "DYJetsToLL - "+str(int(integralSF['DYJetsToLL']+integralSF['DYJetsToLL_M-4to50'])), "f");
lgSF.AddEntry(histMass['WJetsToLNu'], "WJetsToLNu - "+str(int(integralSF['WJetsToLNu'])), "f");
lgSF.AddEntry(histMass['Diboson'], "Diboson - "+str(int(integralSF['Diboson'])), "f");
nbintcp = sig.GetNbinsX()
lgSF.AddEntry(sig, "TCP_"+massTCP+" - "+str(int(sig.Integral())), "f");
lgSF.AddEntry(errMass, "Bkg. Uncert.", "f")
lgSF.AddEntry(projyNew, "Bkg. Predicted - "+str(int(projyNew.Integral())), "l")

myPlotFunc.drawPad1("var", logy = True)
tmpStack.Draw("hist")
tmpStack.SetMinimum(1)
tmpStack.SetMaximum(1E4)
projyNew.Draw("same hist")
errMass.Draw("same E20P")
sig.Draw("same hist")
lgSF.Draw("same")
c1.cd()
myPlotFunc.drawPad2()
sbhist = myPlotFunc.drawSOverB(projyNew, sig, [0,"M_{vis.} (GeV)"])
sbhist.Draw()

c1.SaveAs(path+"/"+iteration+"_"+DR+"_SR_"+FFver+".png")
c1.Print(path+"/"+iteration+"_"+DR+"_"+FFver+".pdf")
c1.Clear()

l = ROOT.TLegend(0.15,0.15,0.85,0.85)

for j in range(projyNew.GetNbinsX()):
	l.AddEntry(projyNew, "Bin"+str(j+1)+" = "+str(projyNew.GetBinContent(j+1))+"#pm"+str(projyNew.GetBinError(j+1)))
l.AddEntry(projyNew, "Bin 1 = "+str(projyNew.GetBinContent(1)))
l.AddEntry(projyNew, "Bin 2 - 6 = "+str(projyNew.Integral(2,6)))
l.AddEntry(projyNew, "Bin 6 onwards = "+str(projyNew.Integral(6,nbiny)))

l.Draw()
c1.Print(path+"/"+iteration+"_"+DR+"_"+FFver+".pdf")
c1.Clear()

lbkg = ROOT.TLegend(0.15,0.15,0.85,0.85)
for k in range(projyNew.GetNbinsX()):
	lbkg.AddEntry(htot_nQCD, "Bin"+str(k+1)+" = "+str(htot_nQCD.GetBinContent(k+1))+"#pm"+str(htot_nQCD.GetBinError(k+1)))
lbkg.AddEntry(htot_nQCD, "Bin 1 = "+str(htot_nQCD.GetBinContent(1)))
lbkg.AddEntry(htot_nQCD, "Bin 2 - 6 = "+str(htot_nQCD.Integral(2,6)))
lbkg.AddEntry(htot_nQCD, "Bin 6 onwards = "+str(htot_nQCD.Integral(6,nbiny)))

lbkg.Draw()
c1.Print(path+"/"+iteration+"_"+DR+"_"+FFver+".pdf")
c1.Clear()

c1.Print(path+"/"+iteration+"_"+DR+"_"+FFver+".pdf]")

print("output = "+path+"/appliedFf_"+DR+"_v"+FFver+".root")
print("histName = appliedFF_"+DR)
#