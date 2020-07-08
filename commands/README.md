# Commands for ApPredict

Here is a list of the commands used to generate the simulation data.

## azithromycin
`./ApPredict.sh --model 8 --pacing-freq 0.5 --pic50-herg 4.15 --pic50-spread-herg 0.139 --pic50-iks 3.33 --pic50-spread-iks 0.127 --pic50-nal 3.72 --pic50-spread-nal 0.15 --pic50-ito 4.05 --pic50-spread-ito 0.15 --plasma-conc-high 100 --plasma-conc-count 19 --plasma-conc-logscale True --no-downsampling True --credible-intervals 60 70 80 90 95 --brute-force 1000 --output-dir AZ &> testoutput/AZ.txt &`

## chloroquine
`./ApPredict.sh --model 8 --pacing-freq 0.5 --pic50-herg 5.16 --pic50-spread-herg 0.139 --pic50-ik1 4.97 --pic50-spread-ik1 0.15 --plasma-conc-high 100 --plasma-conc-count 19 --plasma-conc-logscale True --no-downsampling True --credible-intervals 60 70 80 90 95 --brute-force 1000 --output-dir CQ &> testoutput/CQ.txt &`

## halofantrine
`./ApPredict.sh --model 8 --pacing-freq 0.5 --pic50-herg 6.42 --pic50-spread-herg 0.139 --pic50-cal 5.72 --pic50-spread-cal 0.181 --pic50-na 3.48 --pic50-spread-na 0.141 --plasma-conc-high 100 --plasma-conc-count 19 --plasma-conc-logscale True --no-downsampling True --credible-intervals 60 70 80 90 95 --brute-force 1000 --output-dir HAL &> testoutput/HAL.txt &`

## hydroxychloroquine
`./ApPredict.sh --model 8 --pacing-freq 0.5 --pic50-herg 5.25 --pic50-spread-herg 0.139 --pic50-cal 4.57 --pic50-spread-cal 0.181 --pic50-iks 5.03 --pic50-spread-iks 0.127 --plasma-conc-high 100 --plasma-conc-count 19 --plasma-conc-logscale True --no-downsampling True --credible-intervals 60 70 80 90 95 --brute-force 1000 --output-dir HCQ &> testoutput/HCQ.txt &`

## moxifloxacin
`./ApPredict.sh --model 8 --pacing-freq 0.5 --pic50-herg 4.03 --pic50-spread-herg 0.139 --pic50-iks 4.30 --pic50-spread-iks 0.127 --pic50-nal 3.42 --pic50-spread-nal 0.15 --plasma-conc-high 100 --plasma-conc-count 19 --plasma-conc-logscale True --no-downsampling True --credible-intervals 60 70 80 90 95 --brute-force 1000 --output-dir MOX &> testoutput/MOX.txt &`

## quinine
`./ApPredict.sh --model 8 --pacing-freq 0.5 --pic50-herg 5.29 --pic50-spread-herg 0.139 --pic50-cal 4.57 --pic50-spread-cal 0.181 --pic50-na 4.62 --pic50-spread-na 0.141 --pic50-iks 4.43 --pic50-spread-iks 0.127 --pic50-ito 4.10 --pic50-spread-ito 0.15 --plasma-conc-high 100 --plasma-conc-count 19 --plasma-conc-logscale True --no-downsampling True --credible-intervals 60 70 80 90 95 --brute-force 1000 --output-dir QUIN &> testoutput/QUIN.txt &`

## hydroxychloroquine/azithromycin
`./ApPredict.sh --model 8 --pacing-freq 0.5 --pic50-herg 5.25 --pic50-spread-herg 0.139 --pic50-cal 4.57 --pic50-spread-cal 0.181 --pic50-iks 5.03 --pic50-spread-iks 0.127 --pic50-drug-two-herg 4.15 --pic50-spread-drug-two-herg 0.139 --pic50-drug-two-iks 3.33 --pic50-spread-drug-two-iks 0.127 --pic50-drug-two-nal 3.72 --pic50-spread-drug-two-nal 0.15 --pic50-drug-two-ito 4.05 --pic50-spread-drug-two-ito 0.15 --drug-two-conc-factor 1.59 --plasma-conc-high 100 --plasma-conc-count 19 --plasma-conc-logscale True --no-downsampling True --credible-intervals 60 70 80 90 95 --brute-force 1000 --output-dir HCQ_AZ &> testoutput/HCQ_AZ.txt &`

## hydroxychloroquine/halofantrine
`./ApPredict.sh --model 8 --pacing-freq 0.5 --pic50-herg 5.25 --pic50-spread-herg 0.139 --pic50-cal 4.57 --pic50-spread-cal 0.181 --pic50-iks 5.03 --pic50-spread-iks 0.127 --pic50-drug-two-herg 6.42 --pic50-spread-drug-two-herg 0.139 --pic50-drug-two-cal 5.72 --pic50-spread-drug-two-cal 0.181 --pic50-drug-two-na 3.48 --pic50-spread-drug-two-na 0.141 --drug-two-conc-factor 0.47 --plasma-conc-high 100 --plasma-conc-count 19 --plasma-conc-logscale True --no-downsampling True --credible-intervals 60 70 80 90 95 --brute-force 1000 --output-dir HCQ_HAL &> testoutput/HCQ_HAL.txt &`

## hydroxychloroquine/moxifloxacin
`./ApPredict.sh --model 8 --pacing-freq 0.5 --pic50-herg 5.25 --pic50-spread-herg 0.139 --pic50-cal 4.57 --pic50-spread-cal 0.181 --pic50-iks 5.03 --pic50-spread-iks 0.127 --pic50-drug-two-herg 4.03 --pic50-spread-drug-two-herg 0.139 --pic50-drug-two-iks 4.30 --pic50-spread-drug-two-iks 0.127 --pic50-drug-two-nal 3.42 --pic50-spread-drug-two-nal 0.15 --drug-two-conc-factor 3.37 --plasma-conc-high 100 --plasma-conc-count 19 --plasma-conc-logscale True --no-downsampling True --credible-intervals 60 70 80 90 95 --brute-force 1000 --output-dir HCQ_MOX &> testoutput/HCQ_MOX.txt &`

## lopinavir/ritonavir
`./ApPredict.sh --model 8 --pacing-freq 0.5 --pic50-herg 5.29 --pic50-spread-herg 0.139 --pic50-cal 4.81 --pic50-spread-cal 0.181 --pic50-drug-two-herg 5.29 --pic50-spread-drug-two-herg 0.139 --pic50-drug-two-cal 5.08 --pic50-spread-drug-two-cal 0.181 --pic50-drug-two-nal 5.14 --pic50-spread-drug-two-nal 0.15 --drug-two-conc-factor 0.62 --plasma-conc-high 100 --plasma-conc-count 19 --plasma-conc-logscale True --no-downsampling True --credible-intervals 60 70 80 90 95 --brute-force 1000 --output-dir LOP_RIT &> testoutput/LOP_RIT.txt &`

# Supplementary commands for Figure 1

Figure 1 requires action potential waveforms which can be generated quickly using:

## azithromycin
./ApPredict.sh --model 8 --pacing-freq 0.5 --pic50-herg 4.15 --pic50-spread-herg 0.139 --pic50-iks 3.33 --pic50-spread-iks 0.127 --pic50-nal 3.72 --pic50-spread-nal 0.15 --pic50-ito 4.05 --pic50-spread-ito 0.15 --plasma-concs 1.937 3.874 5.811 7.748 19.37 --no-downsampling True --output-dir AZ_supp &> testoutput/AZ_supp.txt &

## chloroquine
./ApPredict.sh --model 8 --pacing-freq 0.5 --pic50-herg 5.16 --pic50-spread-herg 0.139 --pic50-ik1 4.97 --pic50-spread-ik1 0.15 --plasma-concs 0.66 1.32 1.98 2.64 6.6 --no-downsampling True --output-dir CQ_supp &> testoutput/CQ_supp.txt &

## halofantrine
./ApPredict.sh --model 8 --pacing-freq 0.5 --pic50-herg 6.42 --pic50-spread-herg 0.139 --pic50-cal 5.72 --pic50-spread-cal 0.181 --pic50-na 3.48 --pic50-spread-na 0.141 --plasma-concs 0.57 1.14 1.71 2.28 5.7 --no-downsampling True --output-dir HAL_supp &> testoutput/HAL_supp.txt &

## hydroxychloroquine
./ApPredict.sh --model 8 --pacing-freq 0.5 --pic50-herg 5.25 --pic50-spread-herg 0.139 --pic50-cal 4.57 --pic50-spread-cal 0.181 --pic50-iks 5.03 --pic50-spread-iks 0.127 --plasma-concs 1.22 2.44 3.66 4.88 12.2 --no-downsampling True --output-dir HCQ_supp &> testoutput/HCQ_supp.txt &

## moxifloxacin
./ApPredict.sh --model 8 --pacing-freq 0.5 --pic50-herg 4.03 --pic50-spread-herg 0.139 --pic50-iks 4.30 --pic50-spread-iks 0.127 --pic50-nal 3.42 --pic50-spread-nal 0.15 --plasma-concs 4.111 8.222 12.333 16.444 41.11 --no-downsampling True --output-dir MOX_supp &> testoutput/MOX_supp.txt &

## quinine
./ApPredict.sh --model 8 --pacing-freq 0.5 --pic50-herg 5.29 --pic50-spread-herg 0.139 --pic50-cal 4.57 --pic50-spread-cal 0.181 --pic50-na 4.62 --pic50-spread-na 0.141 --pic50-iks 4.43 --pic50-spread-iks 0.127 --pic50-ito 4.10 --pic50-spread-ito 0.15 --plasma-concs 3.9567 7.9134 11.8701 15.8268 39.567 --no-downsampling True --output-dir QUIN_supp &> testoutput/QUIN_supp.txt &

## hydroxychloroquine/azithromycin
./ApPredict.sh --model 8 --pacing-freq 0.5 --pic50-herg 5.25 --pic50-spread-herg 0.139 --pic50-cal 4.57 --pic50-spread-cal 0.181 --pic50-iks 5.03 --pic50-spread-iks 0.127 --pic50-drug-two-herg 4.15 --pic50-spread-drug-two-herg 0.139 --pic50-drug-two-iks 3.33 --pic50-spread-drug-two-iks 0.127 --pic50-drug-two-nal 3.72 --pic50-spread-drug-two-nal 0.15 --pic50-drug-two-ito 4.05 --pic50-spread-drug-two-ito 0.15 --drug-two-conc-factor 1.59 --plasma-concs 1.22 2.44 3.66 4.88 12.2 --no-downsampling True --output-dir HCQ_AZ_supp &> testoutput/HCQ_AZ_supp.txt &

## hydroxychloroquine/halofantrine
./ApPredict.sh --model 8 --pacing-freq 0.5 --pic50-herg 5.25 --pic50-spread-herg 0.139 --pic50-cal 4.57 --pic50-spread-cal 0.181 --pic50-iks 5.03 --pic50-spread-iks 0.127 --pic50-drug-two-herg 6.42 --pic50-spread-drug-two-herg 0.139 --pic50-drug-two-cal 5.72 --pic50-spread-drug-two-cal 0.181 --pic50-drug-two-na 3.48 --pic50-spread-drug-two-na 0.141 --drug-two-conc-factor 0.47 --plasma-concs 1.22 2.44 3.66 4.88 12.2 --no-downsampling True --output-dir HCQ_HAL_supp &> testoutput/HCQ_HAL_supp.txt &

## hydroxychloroquine/moxifloxacin
./ApPredict.sh --model 8 --pacing-freq 0.5 --pic50-herg 5.25 --pic50-spread-herg 0.139 --pic50-cal 4.57 --pic50-spread-cal 0.181 --pic50-iks 5.03 --pic50-spread-iks 0.127 --pic50-drug-two-herg 4.03 --pic50-spread-drug-two-herg 0.139 --pic50-drug-two-iks 4.30 --pic50-spread-drug-two-iks 0.127 --pic50-drug-two-nal 3.42 --pic50-spread-drug-two-nal 0.15 --drug-two-conc-factor 3.37 --plasma-concs 1.22 2.44 3.66 4.88 12.2 --no-downsampling True --output-dir HCQ_MOX_supp &> testoutput/HCQ_MOX_supp.txt &

## lopinavir/ritonavir
./ApPredict.sh --model 8 --pacing-freq 0.5 --pic50-herg 5.29 --pic50-spread-herg 0.139 --pic50-cal 4.81 --pic50-spread-cal 0.181 --pic50-drug-two-herg 5.29 --pic50-spread-drug-two-herg 0.139 --pic50-drug-two-cal 5.08 --pic50-spread-drug-two-cal 0.181 --pic50-drug-two-nal 5.14 --pic50-spread-drug-two-nal 0.15 --drug-two-conc-factor 0.62 --plasma-concs 0.704 1.408 2.112 2.816 7.04 --no-downsampling True --output-dir LOP_RIT_supp &> testoutput/LOP_RIT_supp.txt &
