### Read Data
setwd("C:\\Users\\msardar2\\Google Drive\\Brightway2\\organic_analysis")

setwd("C:\\Users\\msmsa\\Google Drive\\Brightway2\\organic_analysis")
data = read.csv('MC_results Nov 15_ both.csv')

### Showing the Tie ranks and histograms
### BU1
par(mfrow=c(1,1))
p1=hist(x = data$GWP_BU1,breaks = c(seq(-1200,200,50)))
p2=hist(x = data$GWP_BU0,breaks = c(seq(-1400,0,50)))

plot(p1, col = rgb(0,1,0,0.4), ylim = c(0,4000),
     xlim = c(-1200,200), main = 'GWP of compost use', 
     xlab = 'GWP Kg CO2e per Mg compost')
plot(p2,col = rgb(1,0,0,0.4),add=T)
legend('topleft',legend=c("ADC Scenario","Soil amendment Scenario"),
       bty = "n",pch =c(15, 15),
       col=c(rgb(1,0,0,0.4),rgb(0,1,0,0.4)))







### 
library(corrplot)
data$dif_gwp = data$GWP_BU0 - data$GWP_BU1
data$dif_acid = data$Acidification_BU0 - data$Acidification_BU1
data$dif_Eutro = data$Eutrophication_BU0 - data$Eutrophication_BU1
data$dif_CED = data$CED_BU0 - data$CED_BU1

data_cor<-data[11:43]
cor_data=data.frame(cor(x=data_cor$dif_gwp,data_cor))
data_cor = data_cor[c(abs(cor_data) > 0.10)]
corrplot(cor(data_cor),method = "number")
CC<-cor(data_cor$dif_gwp,data_cor)
par(mfrow=c(1,1),
    mar=c(6,12,2,2))
A = cor(data_cor$dif_gwp,data_cor)
A = A[,-length(A)]
barplot(A,
        horiz = TRUE,
        xlim = c(-1,1),
        las=1,
        xlab = 'Corrolation with the difference in GWP of the scenarios')



data_cor<-data[c(11:42,44)]
cor_data=data.frame(cor(x=data_cor$dif_acid,data_cor))

data_cor<-data[c(11:42,45)]
cor_data=data.frame(cor(x=data_cor$dif_Eutro,data_cor))


data_cor<-data[c(11:42,46)]
cor_data=data.frame(cor(x=data_cor$dif_CED,data_cor))










######################
##############
#########
### Contour plot
install.packages('plotly')
library(plotly)
Sys.setenv("plotly_username"="msm_sardar")
Sys.setenv("plotly_api_key"="1sn2feGLOWDTIeCSpSRJ")

data_contour = read.csv('contour Nov15_ peat dens_sub.csv')

f <- list(
  family = "Calibri",
  size = 60,
  color = 'black')
f2 <- list(
  family = "Calibri",
  size = 55,
  color = 'black')


xlab <- list(
  title = "Peat Density (kg/m3)",
  titlefont = f,
  tickfont = f2)

ylab <- list(
  title = "Peat Substitution Factor",
  titlefont = f,
  tickfont = f2)

m <- list(
  l = 35,
  r = 20,
  b = 35,
  t = 60)


plot_ly(
  y = seq(0, 1, length.out = 10),
  x = seq(100, 600, length.out = 10), 
  z = matrix(data_contour$Dif_gwp,nrow = 10,ncol = 10),
  type = "contour",
  colorscale='Jet',
  contours = list(start = -500,end = 500,size=100,showlabels = TRUE),
  color = I("black"),
  autosize = F, width = 1200, height = 1200) %>%
  layout(
    font = f2,
    xaxis = xlab,
    yaxis = ylab,
    legend = f2,
    margin = m)%>%
  add_trace(x = c(100, 600),name = '', y = c(0.9, 0.9), type = "scatter", mode = "lines",color = I('white'),
            line = list( width=3, dash='dash'))%>%
  add_trace(x = c(200, 200),name = '', y = c(0, 1), type = "scatter", mode = "lines",color = I('white'),
            line = list( width=3, dash='dash'))

######################################
########################
### Carbon storage in LF vs carbon content
data_contour = read.csv('contour Nov15 _ c input _ c storage.csv')

xlab <- list(
  title = "C storage in LF (%)",
  titlefont = f,
  tickfont = f2)

ylab <- list(
  title = "Compost Carbon Content",
  titlefont = f,
  tickfont = f2)

m <- list(
  l = 35,
  r = 20,
  b = 35,
  t = 60)

plot_ly(
  y = seq(0.1, 0.47, length.out = 10),
  x = seq(55, 100, length.out = 10), 
  z = matrix(data_contour$Dif_gwp,nrow = 10,ncol = 10),
  type = "contour",
  colorscale='Jet',
  contours = list(start = -500,end = 500,size=100,showlabels = TRUE),
  color = I("black"),
  autosize = F, width = 1200, height = 1200) %>%
  layout(
    font = f2,
    xaxis = xlab,
    yaxis = ylab,
    legend = f2,
    margin = m) %>%
add_trace(x = c(55, 100),name = '', y = c(0.3, 0.3), type = "scatter", mode = "lines",color = I('white'),
                      line = list( width=3, dash='dash'))%>%
add_trace(x = c(90, 90),name = '', y = c(0.1, 0.47), type = "scatter", mode = "lines",color = I('white'),
                      line = list( width=3, dash='dash'))


######################################
########################
### Moisure content of compost vs carbon content
data_contour = read.csv('contour Nov15 _ c input _Moisture .csv')

xlab <- list(
  title = "Compost Moisture content",
  titlefont = f,
  tickfont = f2)

ylab <- list(
  title = "Compost Carbon Content",
  titlefont = f,
  tickfont = f2)

m <- list(
  l = 35,
  r = 20,
  b = 35,
  t = 60)

plot_ly(
  x  = seq(0.18, 0.67, length.out = 10),
  y = seq(0.10, 0.47, length.out = 10), 
  z = matrix(data_contour$Dif_gwp,nrow = 10,ncol = 10),
  type = "contour",
  colorscale='Jet',
  contours = list(start = -500,end = 500,size=100,showlabels = TRUE),
  color = I("black"),
  autosize = F, width = 700, height = 700) %>%
  layout(
    font = f,
    xaxis = xlab,
    yaxis = ylab,
    legend = f,
    margin = m)%>%
  add_trace(x = c(0.18, 0.67),name = '', y = c(.30, 0.3), type = "scatter", mode = "lines",color = I('white'),
            line = list( width=3, dash='dash'))%>%
  add_trace(x = c(0.45, 0.45),name = '', y = c(0.10, 0.47), type = "scatter", mode = "lines",color = I('white'),
            line = list( width=3, dash='dash'))

######################################
########################
### Moisure content of compost vs Peat density
data_contour = read.csv('contour Nov15_ MFEN NCont.csv')

xlab <- list(
  title = "Compost nitrogen content",
  titlefont = f,
  tickfont = f2)

ylab <- list(
  title = "MFEN",
  titlefont = f,
  tickfont = f2)

leglab<- list(
  title = "Compost Moisture content",
  titlefont = f,
  tickfont = f2)

m <- list(
  l = 35,
  r = 20,
  b = 35,
  t = 60)

plot_ly(
  y = seq(0,1, length.out = 10),
  x = seq(0.0051,0.028, length.out = 10), 
  z = matrix(data_contour$Dif_gwp,nrow = 10,ncol = 10),
  type = "contour",
  colorscale='Jet',
  contours = list(start = -500,end = 500,size=30,showlabels = TRUE),
  color = I("black"),
   width = 700, height = 700) %>%
  layout(
    font = f,
    xaxis = xlab,
    yaxis = ylab,
    legend = leglab,
    margin = m)%>%
  add_trace(x = c(0.015,0.015),name = '', y = c(0,1), type = "scatter", mode = "lines",color = I('white'),
            line = list( width=3, dash='dash'))%>%
  add_trace(x = c(0.0051, 0.028),name = '', y = c(0.6, 0.6), type = "scatter", mode = "lines",color = I('white'),
            line = list( width=3, dash='dash'))









setwd("C:\\Users\\msardar2\\Google Drive\\Brightway2\\organic_analysis")
setwd("C:\\Users\\msmsa\\Google Drive\\Brightway2\\organic_analysis")
data = read.csv('distibution.csv')
par(mfrow=c(1,1))
par(mgp=c(2,2,0),las=0)
boxplot(data[1:4],
        col="white",
        border="black",
        xaxt='n',
        yaxt='n',
        ylim=c(-500,1500),
        ylab=expression(paste('GWP (',kgCO[2],'e)')))

axis(1,1:4, c("ADC \n \n",
                    "Soil amendment \n fertilizer offset \n",
                    "Soil amendment \n peat offset \n",
                    "Soil amendment \n both fertilizer \n and peat offset"), mgp=c(3, 3, 0))
axis(2, mgp=c(3, 1, 0))



boxplot(data[5:8],
        col="white",
        border="black",
        xaxt='n',
        yaxt='n',
        #ylim=c(-500,1500),
        ylab=expression(paste('Acidification (',kgSO[2],'e)')))

axis(1,1:4, c("ADC \n \n",
              "Soil amendment \n fertilizer offset \n",
              "Soil amendment \n peat offset \n",
              "Soil amendment \n both fertilizer \n and peat offset"), mgp=c(3, 3, 0))
axis(2, mgp=c(3, 1, 0))


boxplot(data[9:12],
        col="white",
        border="black",
        xaxt='n',
        yaxt='n',
        #ylim=c(-500,1500),
        ylab=expression(paste('Eutrophication ( ',kgN,'e)')))

axis(1,1:4, c("ADC \n \n",
              "Soil amendment \n fertilizer offset \n",
              "Soil amendment \n peat offset \n",
              "Soil amendment \n both fertilizer \n and peat offset"), mgp=c(3, 3, 0))
axis(2, mgp=c(3, 1, 0))


boxplot(data[13:16],
        col="white",
        border="black",
        xaxt='n',
        yaxt='n',
        ylim=c(-8500,500),
        ylab=expression(paste('CED ( ',MJ,'e)')))

axis(1,1:4, c("ADC \n \n",
              "Soil amendment \n fertilizer offset \n",
              "Soil amendment \n peat offset \n",
              "Soil amendment \n both fertilizer \n and peat offset"), mgp=c(3, 3, 0))
axis(2, mgp=c(3, 1, 0))

boxplot(data[17:20],
        col="white",
        border="black",
        xaxt='n',
        yaxt='n',
        #ylim=c(-8500,500),
        ylab=expression(paste('GWP (',kgCO[2],'e)')))

axis(1,1:4, c("ADC \n \n",
              "Soil amendment \n fertilizer offset \n",
              "Soil amendment \n peat offset \n",
              "Soil amendment \n both fertilizer \n and peat offset"), mgp=c(3, 3, 0))
axis(2, mgp=c(3, 1, 0))


boxplot(data[21:24],
        col="white",
        border="black",
        xaxt='n',
        yaxt='n',
        ylim=c(-500,1500),
        ylab=expression(paste('GWP (',kgCO[2],'e)')))

axis(1,1:4, c("ADC \n \n",
              "Soil amendment \n fertilizer offset \n",
              "Soil amendment \n peat offset \n",
              "Soil amendment \n both fertilizer \n and peat offset"), mgp=c(3, 3, 0))
axis(2, mgp=c(3, 1, 0))

boxplot(data[25:28],
        col="white",
        border="black",
        xaxt='n',
        yaxt='n',
        #ylim=c(-1500,300),
        ylab=expression(paste('GWP (',kgCO[2],'e)')))

axis(1,1:4, c("ADC \n \n",
              "Soil amendment \n fertilizer offset \n",
              "Soil amendment \n peat offset \n",
              "Soil amendment \n both fertilizer \n and peat offset"), mgp=c(3, 3, 0))
axis(2, mgp=c(3, 1, 0))

