import sys, os
import ROOT
import myPlotFunc
import argparse

path = '/Users/muti/Documents/Analysis/studyCleanedTaus/'

ver = "v1"
iteration = "MCOnly"
tcpMass = "m30"
dataver = "v16"

r = {
    'MuonPt'    : [10, "Pt(GeV)", 250],
    'Muon1Pt'   : [20, "Pt(GeV)", 500],
    'Muon2Pt'   : [20, "Pt(GeV)", 500],
    'ElectronPt': [20, "Pt(GeV)", 500],
    'Lepton1Pt' : [20, "Pt(GeV)", 500],
    'Lepton2Pt'	: [20, "Pt(GeV)", 500],
    'TauPt'     : [10, "Pt(GeV)", 250],
    'TauPt0'        : [20, "Pt(GeV)", 500],
    'TauPt1'        : [20, "Pt(GeV)", 500],
    'TauPt10'       : [20, "Pt(GeV)", 500],
    'JetPt'     : [50, "Pt(GeV)", 2000],
    'MetPt'     : [20, "Pt(GeV)", 500],
    'dRl'       : [1, "dR", 5],
    'dRj'       : [1, "dR", 5],
    'dPhil'     : [5, "dPhi", 3.5],
    'dPhij'     : [5, "dphi", 3.5],
    'Mt'        : [5, "Mt(GeV)", 150],
    'Nj'        : [1, "N_{jet}", 10],
    'Mass'      : [5, "M_{vis}(GeV)", 100],
    'lowMET'    : [5, "M_{vis}(GeV)", 100],
    'dRcut'     : [5, "M_{vis}(GeV)", 100],
    'lowMt'     : [5, "M_{vis}(GeV)", 100],
    'mTcut'     : [5, "M_{vis}(GeV)", 100],
    'highMET'   : [5, "M_{vis}(GeV)", 100],
    'Metcut'    : [5, "M_{vis}(GeV)", 100],
    'highMt'    : [5, "M_{vis}(GeV)", 100],
    'dPhicut'   : [5, "M_{vis}(GeV)", 100],
    'Trigger'   : [1, "Triggers", 8]
}

ROOT.TH1.AddDirectory(0)

def get_histograms(H):
	for h in H:
		for variable in VARIABLE:
			hist_to_plot.append(str(h)+"_"+variable)

	return hist_to_plot


def color_hist(s, h):
	if s == "DYJetsToLL":
		h.SetFillColor(ROOT.TColor.GetColor("#E15759"))
	if s == "DYJetsToLL_M-4to50":
		h.SetFillColor(ROOT.TColor.GetColor("#FF9D9A"))
	if s == "TTJets":
		h.SetFillColor(ROOT.TColor.GetColor("#F1CE63"))
	if s == "Diboson":
		h.SetFillColor(ROOT.TColor.GetColor("#A0CBE8"))
	if s == "QCD":
		h.SetFillColor(ROOT.TColor.GetColor("#BaB0AC"))
	if s == "WJetsToLNu":
		h.SetFillColor(ROOT.TColor.GetColor("#59A14F"))


def get_stack(toPlot, samp):
	tmp_stack = ROOT.THStack("Bkg",toPlot+";"+str(r[toRebin[-1]][1])+";Events / "+str(r[toRebin[-1]][0])+" GeV")
	for s in samp:
		h = f.Get(s+"_"+toPlot)
		h.Rebin(r[toRebin[-1]][0])
		color_hist(s,h)
		tmp_stack.Add(h)

	tmp_stack.SetMinimum(1)
	tmp_h = tmp_stack.GetStack().Last()
	tmp_h = myPlotFunc.plotStyle(tmp_h, r[toRebin[-1]][0], 12, 12, 3, r[toRebin[-1]][1], 3244, draw = "E20P")

	return tmp_stack, tmp_h


def get_signal(toPlot, sig):
	s1 = f.Get(sig[0]+"_"+toPlot)
	s2 = f.Get(sig[1]+"_"+toPlot)

	sig = s1.Clone("TCP")
	sig.Sumw2()
	sig.Add(s2)
	sig.Rebin(r[toRebin[-1]][0])

	sig = myPlotFunc.plotStyle(sig, r[toRebin[-1]][0], 4, 0)

	return sig

def get_data(toPlot):
	d1 = ROOT.TFile("h_debugMuTau_HighHT_Data_SingleMuon_"+dataver+".root");
	d2 = ROOT.TFile("h_debugMuTau_HighHT_Data_JetHT_"+dataver+".root");

	data1 = d1.Get(toPlot)
	data2 = d2.Get(toPlot)
	data = data1.Clone("data")
	data.Add(data2)

	return data


def draw_hist_wstack(hstack, hbkg, h1):
	"""
	short description 
	extended description 

	hstack (ROOT.THStack): Description 


	returns 
	None 

	"""

	hstack.Draw("hist")
	hbkg.Draw("same E20P")
	h1.Draw("same hist E")

	if hstack.GetMaximum() <= h1.GetMaximum():
		hstack.SetMaximum(h1.GetMaximum()*10)

	if hstack.GetMaximum() >= 10000:
		hstack.GetYaxis().SetMaxDigits(4)
	else: hstack.GetYaxis().SetMaxDigits(3)
	

if __name__ == "__main__":
	parser = argparse.ArgumentParser(description="To plot histograms with stacked MC backgrounds and data (for non-SR)")
	parser.add_argument("-l", "--listhist", nargs="+", type=str, help="list of histograms to plot")
	parser.add_argument("-r", "--region", nargs="+", type=str, help="Region to plot")
	parser.add_argument("-d","--data", action="store_true", dest="data", help="Plot MC and data")
	parser.add_argument("-m","--mc", action="store_true", dest="mc", help="Plot MC only")
	args = parser.parse_args(args=None if sys.argv[1:] else ['--help'])

	SAMPLES = ['Diboson','WJetsToLNu','DYJetsToLL','DYJetsToLL_M-4to50','TTJets','QCD']
	SIGNALS = ['TCP_Ntuple_'+tcpMass+'_HT-100to400','TCP_Ntuple_'+tcpMass+'_HT-400toInf']
	VARIABLE = ['Mass', 'Lepton1Pt', 'Lepton2Pt', 'JetPt', 'Mt', 'MetPt', 'Nj']

	if args.region is not None:
		reg = args.region
		hist_to_plot = []
		hist_to_plot = get_histograms(reg)
	elif args.listhist is not None:
		hist_to_plot = arg.listhist
	else:
		print("Must provide regions or histograms to plot")
		print("Exiting")
		exit()
	
	print(hist_to_plot)

	c1 = ROOT.TCanvas("c1","c1",850, 850)
	c1.SetLogy()
	c1.cd()

	if args.mc:

		for hist in hist_to_plot:
			f = ROOT.TFile("h_"+hist+"_"+iteration+"_"+ver+".root")
			toRebin = hist.split("_")
			
			stack = get_stack(hist, SAMPLES)
			signal = get_signal(hist, SIGNALS)

			myPlotFunc.drawPad1(r[toRebin[-1]], logy = True)
			draw_hist_wstack(stack[0], stack[1], signal)
			c1.cd()
			myPlotFunc.drawPad2()

			sbhist = myPlotFunc.drawSOverB(stack[1], signal, r[toRebin[-1]])
			sbhist.Draw()

			c1.SaveAs(path+"test_"+hist+"_MCOnly.png")
			c1.Clear()

		# print(dir(ROOT.TColor))

	if args.data :

		for hist in hist_to_plot:
			f = ROOT.TFile("h_"+hist+"_"+iteration+"_"+ver+".root")
			toRebin = hist.split("_")
			
			stack = get_stack(hist, SAMPLES)
			data = get_data(hist)

			draw_hist_wstack(stack, data, "Data/MC")
