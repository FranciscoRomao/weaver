python run.py configs/13_isca_maintable/arb/baker.yml & 
python run.py configs/13_isca_maintable/arb/faa.yml &
python run.py configs/13_isca_maintable/arb/geyser.yml &
python run.py configs/13_isca_maintable/arb/sc.yml &
python run.py configs/13_isca_maintable/arb/fpqac.yml &

python run.py configs/13_isca_maintable/qaoa/baker.yml &
python run.py configs/13_isca_maintable/qaoa/faa.yml &
python run.py configs/13_isca_maintable/qaoa/geyser.yml &
python run.py configs/13_isca_maintable/qaoa/sc.yml &
python run.py configs/13_isca_maintable/qaoa/fpqac.yml &

python run.py configs/13_isca_maintable/qsim/baker.yml &
python run.py configs/13_isca_maintable/qsim/faa.yml &
python run.py configs/13_isca_maintable/qsim/geyser.yml &
python run.py configs/13_isca_maintable/qsim/sc.yml &
python run.py configs/13_isca_maintable/qsim/fpqac.yml &

wait
