#!/usr/bin/python


def outlierCleaner(predictions, ages, net_worths):
    """
        Clean away the 10% of points that have the largest
        residual errors (difference between the prediction
        and the actual net worth).

        Return a list of tuples named cleaned_data where
        each tuple is of the form (age, net_worth, error).
    """

    cleaned_data = []
    tam=int(0.1*len(ages));


    # Genero la lista de tuplas
    for i in range(0,len(ages)):
        error=abs(predictions[i]-net_worths[i])
        cleaned_data.append((float(ages[i]),float(net_worths[i]), float(error)))

    #La ordeno de manera ascendente respecto al valor absoluto del error
    cleaned_data.sort(key=lambda tup:tup[2])

    #Elimino el ultimo 10% de la lista (elementos con mayor error)
    for i in range(0,tam):
        cleaned_data.pop()


    return cleaned_data
