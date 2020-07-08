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

## HCQ + AZ
`./ApPredict.sh --model 8 --pacing-freq 0.5 --pic50-herg 5.25 --pic50-spread-herg 0.139 --pic50-cal 4.57 --pic50-spread-cal 0.181 --pic50-iks 5.03 --pic50-spread-iks 0.127 --pic50-drug-two-herg 4.15 --pic50-spread-drug-two-herg 0.139 --pic50-drug-two-iks 3.33 --pic50-spread-drug-two-iks 0.127 --pic50-drug-two-nal 3.72 --pic50-spread-drug-two-nal 0.15 --pic50-drug-two-ito 4.05 --pic50-spread-drug-two-ito 0.15 --drug-two-conc-factor 1.59 --plasma-conc-high 100 --plasma-conc-count 19 --plasma-conc-logscale True --no-downsampling True --credible-intervals 60 70 80 90 95 --brute-force 1000 --output-dir HCQ_AZ &> testoutput/HCQ_AZ.txt &`

## HCQ + HAL
`./ApPredict.sh --model 8 --pacing-freq 0.5 --pic50-herg 5.25 --pic50-spread-herg 0.139 --pic50-cal 4.57 --pic50-spread-cal 0.181 --pic50-iks 5.03 --pic50-spread-iks 0.127 --pic50-drug-two-herg 6.42 --pic50-spread-drug-two-herg 0.139 --pic50-drug-two-cal 5.72 --pic50-spread-drug-two-cal 0.181 --pic50-drug-two-na 3.48 --pic50-spread-drug-two-na 0.141 --drug-two-conc-factor 0.47 --plasma-conc-high 100 --plasma-conc-count 19 --plasma-conc-logscale True --no-downsampling True --credible-intervals 60 70 80 90 95 --brute-force 1000 --output-dir HCQ_HAL &> testoutput/HCQ_HAL.txt &`

## HCQ + MOX
`./ApPredict.sh --model 8 --pacing-freq 0.5 --pic50-herg 5.25 --pic50-spread-herg 0.139 --pic50-cal 4.57 --pic50-spread-cal 0.181 --pic50-iks 5.03 --pic50-spread-iks 0.127 --pic50-drug-two-herg 4.03 --pic50-spread-drug-two-herg 0.139 --pic50-drug-two-iks 4.30 --pic50-spread-drug-two-iks 0.127 --pic50-drug-two-nal 3.42 --pic50-spread-drug-two-nal 0.15 --drug-two-conc-factor 3.37 --plasma-conc-high 100 --plasma-conc-count 19 --plasma-conc-logscale True --no-downsampling True --credible-intervals 60 70 80 90 95 --brute-force 1000 --output-dir HCQ_MOX &> testoutput/HCQ_MOX.txt &`

## LOP + RIT
`./ApPredict.sh --model 8 --pacing-freq 0.5 --pic50-herg 5.29 --pic50-spread-herg 0.139 --pic50-cal 4.81 --pic50-spread-cal 0.181 --pic50-drug-two-herg 5.29 --pic50-spread-drug-two-herg 0.139 --pic50-drug-two-cal 5.08 --pic50-spread-drug-two-cal 0.181 --pic50-drug-two-nal 5.14 --pic50-spread-drug-two-nal 0.15 --drug-two-conc-factor 0.62 --plasma-conc-high 100 --plasma-conc-count 19 --plasma-conc-logscale True --no-downsampling True --credible-intervals 60 70 80 90 95 --brute-force 1000 --output-dir LOP_RIT &> testoutput/LOP_RIT.txt &`