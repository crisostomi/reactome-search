import OMPython
import pandas as pd                # dataframes
import matplotlib.pyplot as plt    # plottare grafici
import seaborn as sns              # si basa su plt, ha funzioni piu sofisticate
import os

def load_model(folder_path, file_name, class_name):
    file_path = folder_path + file_name
    dependencies = ["Modelica"]
    for file in os.listdir(folder_path):
        if file.endswith(".mo") and not file == file_name:
            dependencies.append(folder_path + file)

    user_home = os.environ['HOME']
    dependencies.append(user_home + '/Dropbox/Tesisti/software/BioChem-1.0.1/BioChem/package.mo')
    dependencies.append(user_home + '/Dropbox/Tesisti/software/BioChem-1.0.1/new-models/reactions.mo')
    return OMPython.ModelicaSystem(file_path, class_name, dependencies)

# Ritorna un oggetto Pandas DataFrame con all'interno i datapoints ({istante, valore}) delle variabili simulate del modello
def get_solutions(model, variables=[]):
    # recupera la "linea temporale"
    time = model.getSolutions("time")
    # se variables e' vuoto, mettici i nomi di tutte le variabili del sistema
    if len(variables) == 0:
        variables = model.getSolutions()

    # costruisce il dataframe con solo la prima variabile
    solutions = [model.getSolutions(var) for var in variables]
    df = pd.DataFrame({"time": time, "value": solutions[0], "variable": variables[0]})

    # appende al dataframe tutti i dati delle altre variabili
    for i in range(1, len(variables)):
        df = df.append(
            pd.DataFrame({"time": time, "value": solutions[i], "variable": variables[i]}),
            ignore_index=True
        )
    return df

# Prende in input un DataFrame pandas in cui vi sia la colonna "time", e una lista di variabili
# Plotta il moto delle variabili su un grafico in cui le ascisse sono l'asse del tempo e le ordinate l'asse dei valori
# ATTENZIONE: potrebbe perdere di significato se si cerca di plottare variabili in intervalli di valori di dimensione diversa

def plot_solutions(solution_frame, variables=[]):
    if len(variables) == 0:
        sns.lineplot(data=solution_frame, x="time", y="value", hue="variable")
    else:
        sns.lineplot(data=solution_frame[solution_frame['variable'].isin(variables)], x="time", y="value", hue="variable")
    plt.show()