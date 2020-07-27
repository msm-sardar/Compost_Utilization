### Read Data
setwd("C:\\Users\\msardar2\\Google Drive\\Brightway2\\organic_analysis")

setwd("C:/Users/msmsa/Google Drive/Brightway2/Compost_Utilization/Results")
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
  family = "sans serif",
  size = 28,
  color = 'black')
f2 <- list(
  family = "sans serif",
  size = 28,
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
  autosize = F, width = 700, height = 700) %>%
  layout(
    font = f,
    xaxis = xlab,
    yaxis = ylab,
    legend = f,
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
  title = "Compost Carbon Content (%)",
  titlefont = f,
  tickfont = f2)

m <- list(
  l = 35,
  r = 20,
  b = 35,
  t = 60)

plot_ly(
  y = seq(10, 47, length.out = 10),
  x = seq(55, 100, length.out = 10), 
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
    margin = m) %>%
add_trace(x = c(55, 100),name = '', y = c(30, 30), type = "scatter", mode = "lines",color = I('white'),
                      line = list( width=3, dash='dash'))%>%
add_trace(x = c(90, 90),name = '', y = c(10, 47), type = "scatter", mode = "lines",color = I('white'),
                      line = list( width=3, dash='dash'))


######################################
########################
### Moisure content of compost vs carbon content
data_contour = read.csv('contour Nov15 _ c input _Moisture .csv')

xlab <- list(
  title = "Compost Moisture content (%)",
  titlefont = f,
  tickfont = f2)

ylab <- list(
  title = "Compost Carbon Content (%)",
  titlefont = f,
  tickfont = f2)

m <- list(
  l = 35,
  r = 20,
  b = 35,
  t = 60)

plot_ly(
  x  = seq(18, 67, length.out = 10),
  y = seq(10, 47, length.out = 10), 
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
  add_trace(x = c(18, 67),name = '', y = c(30, 30), type = "scatter", mode = "lines",color = I('white'),
            line = list( width=3, dash='dash'))%>%
  add_trace(x = c(45, 45),name = '', y = c(10, 47), type = "scatter", mode = "lines",color = I('white'),
            line = list( width=3, dash='dash'))

######################################
########################
### Moisure content of compost vs Peat density
data_contour = read.csv('contour Nov15_ MFEN NCont.csv')

xlab <- list(
  title = "Compost nitrogen content (%)",
  titlefont = f,
  tickfont = f2)

ylab <- list(
  title = "MFEN",
  titlefont = f,
  tickfont = f2)

m <- list(
  l = 35,
  r = 20,
  b = 35,
  t = 60)

plot_ly(
  y = seq(0,1, length.out = 10),
  x = seq(0.51,2.8, length.out = 10), 
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
    legend = f,
    margin = m)%>%
  add_trace(x = c(1.5,1.5),name = '', y = c(0,1), type = "scatter", mode = "lines",color = I('white'),
            line = list( width=3, dash='dash'))%>%
  add_trace(x = c(0.51, 2.8),name = '', y = c(0.6, 0.6), type = "scatter", mode = "lines",color = I('white'),
            line = list( width=3, dash='dash'))





######################################
########################   Eutrophication
### N content vs N as NO3
data_contour = read.csv('contour Jul23_ NCont_NO3_Eutrophication.csv')

xlab <- list(
  title = "Compost N content (%)",
  titlefont = f,
  tickfont = f2)

ylab <- list(
  title = "Percent of N as NO3 (%)",
  titlefont = f,
  tickfont = f2)

m <- list(
  l = 35,
  r = 20,
  b = 35,
  t = 60)

fig<-plot_ly(
  type = "contour",
  x= seq(2.8,0.51, length.out = 10),
  y = seq(3,87, length.out = 10), 
  z = matrix(data_contour$Dif_Eutrophication,nrow = 10,ncol = 10),
  colorscale='Jet',
  contours = list(start = -10,end = 2,size=1,showlabels = TRUE,tickfont=f),
  color = I("black"),
  width = 700, height = 700) 

fig<-fig%>% colorbar(title = "Elevation \n in meters") 
fig<-fig%>%layout(
    font = f,
    xaxis = xlab,
    yaxis = ylab,
    legend = f,
    tickfont=f,
    margin = m)%>% colorbar(title = "Elevation \n in meters")

fig<-fig%>%add_trace(x = c(0.51, 2.8),name = '', y = c(20, 20), type = "scatter", mode = "lines",color = I('white'),
            line = list( width=3, dash='dash'))

fig<-fig%>%add_trace(fig,x = c(1.5,1.5),name = '', y = c(5,85), type = "scatter", mode = "lines",color = I('white'),
            line = list( width=3, dash='dash'))

fig


######################################
########################   Eutrophication
### N content vs N compost moisture
data_contour = read.csv('contour Jun15_ NCont_moisture_Eutrophication.csv')

xlab <- list(
  title = "Compost N content (%)",
  titlefont = f,
  tickfont = f2)

ylab <- list(
  title = "Compost moisture content (%)",
  titlefont = f,
  tickfont = f2)

m <- list(
  l = 35,
  r = 20,
  b = 35,
  t = 60)

plot_ly(
  x= seq(0.51,2.8, length.out = 10),
  y = seq(18,67, length.out = 10), 
  z = matrix(data_contour$Dif_Eutrophication,nrow = 10,ncol = 10),
  type = "contour",
  colorscale='Jet',
  contours = list(start = -5,end = 2,size=1,showlabels = TRUE),
  color = I("black"),
  width = 700, height = 700) %>%
  layout(
    font = f,
    xaxis = xlab,
    yaxis = ylab,
    legend = f,
    margin = m)%>% 
  add_trace(x = c(0.51, 2.8),name = '', y = c(45,45), type = "scatter", mode = "lines",color = I('white'),
            line = list( width=3, dash='dash'))%>%
  add_trace(x = c(1.5,1.5),name = '', y = c(18,67), type = "scatter", mode = "lines",color = I('white'),
            line = list( width=3, dash='dash'))






######################################
########################  CED
### 
data_contour = read.csv('contour Jun15_CED.csv')

ylab <- list(
  title = "Peat substitution factor",
  titlefont = f,
  tickfont = f2)

xlab <- list(
  title = "Peat density (kg/m3)",
  titlefont = f,
  tickfont = f2)

m <- list(
  l = 35,
  r = 20,
  b = 35,
  t = 60)

plot_ly(
  y= seq(0.22,1, length.out = 10),
  x = seq(100,350, length.out = 10), 
  z = matrix(data_contour$Dif_Eutrophication,nrow = 10,ncol = 10),
  type = "contour",
  colorscale='Jet',
  contours = list(start = 0,end = 6000,size=500,showlabels = TRUE),
  color = I("black"),
  width = 700, height = 700) %>%
  layout(
    font = f,
    xaxis = xlab,
    yaxis = ylab,
    legend = f,
    margin = m)%>% 
  add_trace(x = c(100, 350),name = '', y = c(0.9,0.9), type = "scatter", mode = "lines",color = I('white'),
            line = list( width=3, dash='dash'))%>%
  add_trace(x = c(200,200),name = '', y = c(0.25,1), type = "scatter", mode = "lines",color = I('white'),
            line = list( width=3, dash='dash'))

######################################
########################  Acidification
### 
data_contour = read.csv('contour Jun15_Acidification.csv')

ylab <- list(
  title = "Percent of N as NH3 (%)",
  titlefont = f,
  tickfont = f2)

xlab <- list(
  title = "Compost N content (%)",
  titlefont = f,
  tickfont = f2)

m <- list(
  l = 35,
  r = 20,
  b = 35,
  t = 60)

plot_ly(
  x= seq(0.51,2.8, length.out = 10),
  y = seq(1,50, length.out = 10), 
  z = matrix(data_contour$Dif_Acidification,nrow = 10,ncol = 10),
  type = "contour",
  colorscale='Jet',
  contours = list(start = -2,end = 1,size=0.2,showlabels = TRUE),
  color = I("black"),
  width = 700, height = 700) %>%
  layout(
    font = f,
    xaxis = xlab,
    yaxis = ylab,
    legend = f,
    margin = m)%>% 
  add_trace(x = c(0.51,2.8),name = '', y = c(25,25), type = "scatter", mode = "lines",color = I('white'),
            line = list( width=3, dash='dash'))%>%
  add_trace(x = c(1.5,1.5),name = '', y = c(3,50), type = "scatter", mode = "lines",color = I('white'),
            line = list( width=3, dash='dash'))












































setwd("C:\\Users\\msardar2\\Google Drive\\Brightway2\\organic_analysis")
setwd("C:\\Users\\msmsa\\Google Drive\\Brightway2\\Compost_Utilization\\Results")
data = read.csv('distibution.csv')
par(mfrow=c(1,1))
par(mgp=c(2,2,0),las=0)
boxplot(data[1:4],
        col="white",
        border="black",
        xaxt='n',
        yaxt='n',
        ylim=c(-500,1500),
        ylab=expression(paste('GWP (kg ',CO[2],'e)')))

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
        ylab=expression(paste('Acidification (kg ',SO[2],'e)')))

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
        ylab=expression(paste('GWP (kg ',CO[2],'e)')))

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
        ylab=expression(paste('GWP (kg ',CO[2],'e)')))

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
        ylab=expression(paste('GWP (kg ',CO[2],'e)')))

axis(1,1:4, c("ADC \n \n",
              "Soil amendment \n fertilizer offset \n",
              "Soil amendment \n peat offset \n",
              "Soil amendment \n both fertilizer \n and peat offset"), mgp=c(3, 3, 0))
axis(2, mgp=c(3, 1, 0))










































new_data =   data[c(1:4,13:16)] 
res=cor(new_data)
plot(x=new_data$ADC.scenario..IPCC.2013_GWP..BioCO2.1,
     y=new_data$ADC.scenario..CED,
     xaxt='n', yaxt='n',
     xlab = 'ADC scenario, GWP',ylab = 'ADC scenario, CED')
axis(2, mgp=c(3, 1, 0))
axis(1, mgp=c(3, 1, 0))

plot(x=new_data$Soil.amendment..peat.and.fertilizer..scenario..IPCC.2013_GWP..BioCO2.1,
     y=new_data$Soil.amendment..peat.and.fertilizer..scenario..CED,
     xaxt='n', yaxt='n',
     xlab = 'Soil amendment scenario, GWP',ylab = 'Soil amendment scenario, CED')

axis(2, mgp=c(3, 1, 0))
axis(1, mgp=c(3, 1, 0))


new_data =   data[c(1:4,13:16)] 
res=cor(new_data)
plot(x=data$ADC.scenario..IPCC.2013_GWP..BioCO2.0,
     y=new_data$ADC.scenario..CED,
     xaxt='n', yaxt='n',
     xlab = 'ADC scenario, GWP',ylab = 'ADC scenario, CED')
axis(2, mgp=c(3, 1, 0))
axis(1, mgp=c(3, 1, 0))






data = read.csv('Euro_corr.csv')
Eutrophicaion_corrolation = cor(x=data$X..SWOLF_Eutrophication....SWOLF..,data)




