article = """   título: Experiences in Developing a Distributed Agent-based
                Modeling Toolkit with Python
                resumen: Distributed agent-based modeling (ABM) on high-performance
                computing resources provides the promise of capturing unprecedented details
                of large-scale complex systems. However, the specialized knowledge required
                for developing such ABMs creates barriers to wider adoption and utilization.
                Here we present our experiences in developing an initial implementation of
                Repast4Py, a Python-based distributed ABM toolkit. We build on our
                experiences in developing ABM toolkits, including Repast for High
                Performance Computing (Repast HPC), to identify the key elements of a useful
                distributed ABM toolkit. We leverage the Numba, NumPy, and PyTorch packages
                and the Python C-API to create a scalable modeling system that can exploit
                the largest HPC resources and emerging computing architectures. """

article_words = article.split()
article_lenght = len(article)

summary_index = article_words.index("resumen:")

def article_split(start,end):
    return article_words[start:end]

title = article_split(1,summary_index)

summary = article_split(summary_index+1,article_lenght)

def assign_type(num):
    if num <= 12:
        sentence_type["facil"] += 1
    elif num <= 17:
        sentence_type["aceptable"] += 1
    elif num <= 25:
        sentence_type["dificil"] += 1
    else:
        sentence_type["muy dificil"] += 1


sentence_type = {"facil": 0, "aceptable": 0, "dificil": 0, "muy dificil": 0}

count = 0

for word in title:
    count += 1

if count <= 10:
    print("Titulo: ok")
else:
    print("Titulo: mal")

count = 0

for word in summary:
    count += 1
    if (word.endswith(".")):
        assign_type(count)
        count = 0

print(sentence_type)