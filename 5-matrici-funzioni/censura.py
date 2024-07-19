def censura_parola(parola):
    return parola[0] + "*" * (len(parola) - 2) + parola[-1]

testo = """Moore's law is the observation that the number of transistors
    in an integrated circuit (IC) doubles about every two years. Moore's law
    is an observation and projection of a historical trend. Rather than a law
    of physics, it is an empirical relationship linked to gains from experience
    in production. The observation is named after Gordon Moore, the co-founder of
    Fairchild Semiconductor and Intel (and former CEO of the latter), who in 1965
    posited a doubling every year in the number of components per integrated
    circuit,[a] and projected this rate of growth would continue for at least
    another decade. In 1975, looking forward to the next decade, he revised the
    forecast to doubling every two years, a compound annual growth rate (CAGR)
    of 41%. While Moore did not use empirical evidence in forecasting that the
    historical trend would continue, his prediction has held since 1975 and
    has since become known as a LAW."""

parole_censurate = ["moore","moore's", "law", "semiconductor", "transistors"]

array_testo = testo.split(" ")

for i in range(0, len(array_testo)):
    parola = array_testo[i].lower()
    parola = parola.replace(".","") # rimpiazza il punto con "", quindi togliendolo
    if parola in parole_censurate:
        # array_testo[i] = array_testo[i][0] + "*" * (len(array_testo[i]) - 2) + array_testo[i][-1]
        array_testo[i] = censura_parola(array_testo[i])
print(" ".join(array_testo)) 
