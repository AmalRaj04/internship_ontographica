import pandas as pd

df = pd.read_csv("legacy_internship_records_final.csv")

print("csv loaded")


shape=df.shape
print("rows(entities):",shape[0])
print("columns(properties):",shape[1])

print("properties")
for i,c in enumerate(df.columns):
    print(i,c)

print("missing values")
missing = df.isnull().sum()
print(missing)


print("statistical analysis for numeric properties")
statistics = df.describe()
print(statistics)

print("categorical data distribution")
guild_counts = df['guild'].value_counts()
print(guild_counts)

perf_counts = df['performance_rating'].value_counts()
print(perf_counts)

print("data completeness score")
total_cells = shape[0]*shape[1]
missing_cells = missing.sum()
completness = (total_cells-missing_cells)/total_cells * 100
print(completness)

print("entity identifier analysis")
total_entity = shape[0]
unique_interns = df['intern_id'].nunique()
duplicate_interns = total_entity - unique_interns
print("total intern records:", total_entity)
print("unique intern ids:", unique_interns)
print("duplicate intern ids:", duplicate_interns)



with open("analysis_report.txt", "w", encoding="utf-8") as file:
    file.write("REPORT ON INETERNSHIP RECORD ANALYSIS")

    file.write("\n\nENTITIES AND PROPERTIES\n\n")
    file.write("rows(entities):"+str(shape[0])+"\n") 
    file.write("columns(properties):"+str(shape[1])) 

    file.write("\n\nDATA COMPLETENESS\n\n")
    file.write("total cells:"+str(total_cells)+"\n")
    file.write("missing cells:"+str(missing_cells)+"\n")
    file.write("data completeness score:"+str(completness)+"%")

    file.write("\n\nENTITY IDENTIFIER ANALYSIS\n\n")
    file.write("total intern records:"+str(total_entity)+"\n")
    file.write("unique intern ids:"+str(unique_interns)+"\n")
    file.write("duplicate intern ids:"+str(duplicate_interns))

    file.write("\n\nPROPERTIES\n\n")
    for i,c in enumerate(df.columns):
        file.write(str(i) + " " + c + "\n")

    file.write("\n\nMISSING VALUE ANALYSIS\n\n")
    file.write(str(missing))

    file.write("\n\nSTATISTICAL ANALYSIS\n\n")
    file.write(str(statistics))

    file.write("\n\nGUILD DISTRIBUTION\n\n")
    file.write(str(guild_counts))

    file.write("\n\nPERFORMANCE DISTRIBUTION\n\n")
    file.write(str(perf_counts))

print("report generated sucessfully")