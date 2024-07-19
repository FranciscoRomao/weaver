python run.py configs/25_swap_count/arb/baker.yml & 
python run.py configs/25_swap_count/arb/faa.yml &
python run.py configs/25_swap_count/arb/geyser.yml &
python run.py configs/25_swap_count/arb/sc.yml &
python run.py configs/25_swap_count/arb/fpqac.yml &

python run.py configs/25_swap_count/qaoa/baker.yml &
python run.py configs/25_swap_count/qaoa/faa.yml &
python run.py configs/25_swap_count/qaoa/geyser.yml &
python run.py configs/25_swap_count/qaoa/sc.yml &
python run.py configs/25_swap_count/qaoa/fpqac.yml &

python run.py configs/25_swap_count/qsim/baker.yml &
python run.py configs/25_swap_count/qsim/faa.yml &
python run.py configs/25_swap_count/qsim/geyser.yml &
python run.py configs/25_swap_count/qsim/sc.yml &
python run.py configs/25_swap_count/qsim/fpqac.yml &

wait
