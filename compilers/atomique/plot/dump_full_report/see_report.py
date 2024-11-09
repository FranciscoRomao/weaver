import pickle

pickle_path = "results/dump_full_report/log.pkl"
result = pickle.load(open(pickle_path, "rb"))
print(result)
