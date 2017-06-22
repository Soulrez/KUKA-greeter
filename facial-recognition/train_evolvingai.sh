{ time ../util/align-dlib.py ../data/evolvingai-guest/ align outerEyesAndNose ../data/evolvingai-guest/aligned --size 96 ; } 2> preprocess.txt
{ time ../batch-represent/main.lua -outDir ../data/evolvingai-guest/features -data ../data/evolvingai-guest/aligned ; } 2> representations.txt
{ time ../demos/classifier.py train ../data/evolvingai-guest/features ; } 2> training.txt
