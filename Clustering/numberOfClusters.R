library(factoextra)
library(NbClust)
TrabajoPeru<-data.matrix(TrabajoPeru) #pasar a numerico
df <- scale(TrabajoPeru) #estandarizar

fviz_nbclust(df, kmeans, method = "wss") +geom_vline(xintercept = 3, linetype = 2) + labs(subtitle = "Elbow method")

