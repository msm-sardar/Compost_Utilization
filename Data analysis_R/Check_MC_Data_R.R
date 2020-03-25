
### Read Data
setwd("C:\\Users\\msardar2\\Google Drive\\Brightway2\\organic_analysis")
data = read.csv('MC results_Sep5 _ Clean.csv')

### Summary of data
A <- summary(data)

### Corrolation
B <-cor(data)


### IPCC BU=1 Fertilizer and Peat
plot(y=data$SWOLF_IPCC.BU1,x=data$Land_app.MFEN)

plot(y=data$SWOLF_IPCC.BU0-data$SWOLF_IPCC.BU1,data$initflow.N_cont)


plot(y=data$SWOLF_IPCC.BU0,x=data$Lanfill.percCStor_LF)
C<-cor(data$SWOLF_IPCC.BU1,data)
C<-cor(data$SWOLF_IPCC.BU1,data$Land_app.perN2Oevap)

### Acidificaiton BU=1 Fertilizer and Peat
plot(y=data$SWOLF_Acidification.BU1,x=data$Land_app.perNasNH3fc * data$Land_app.perNH3evap)
### Eutrophication BU=1 Fertilizer and Peat
plot(y=data$SWOLF_Eutrophication.BU1,x=data$initflow.N_cont)
plot(y=data$SWOLF_Eutrophication.BU1,x=data$initflow.N_cont*(data$Land_app.NO3runoff+data$Land_app.NO3leach))
### PhotochemicalSmog BU=1 Fertilizer and Peat
plot(y=data$SWOLF_PhotochemicalSmog.BU1,x=data$initflow.N_cont * data$Land_app.MFEN)

### BU=0 
plot(y=data$SWOLF_IPCC.BU0,x=data$Lanfill.percCStor_LF)
plot(y=data$SWOLF_Acidification.BU0,x=data$Lanfill.percCStor_LF)
plot(y=data$SWOLF_Eutrophication.BU0,x=data$Lanfill.percCStor_LF)
plot(y=data$SWOLF_PhotochemicalSmog.BU0,x=data$Lanfill.percCStor_LF)

### Comparing BU0 and BU=1
plot(y=data$SWOLF_IPCC.BU0,x=data$SWOLF_IPCC.BU1,type='p',asp = 1)
lines(x=data$SWOLF_IPCC.BU1,y=data$SWOLF_IPCC.BU1,col="green")

plot(y=data$SWOLF_Eutrophication.BU0,x=data$SWOLF_Eutrophication.BU1,type='p',asp = 1)
lines(x=data$SWOLF_Eutrophication.BU1,y=data$SWOLF_Eutrophication.BU1,col="green")

plot(y=data$SWOLF_PhotochemicalSmog.BU0,x=data$SWOLF_PhotochemicalSmog.BU1,type='p',asp = 1)
lines(x=data$SWOLF_PhotochemicalSmog.BU1,y=data$SWOLF_PhotochemicalSmog.BU1,col="green")

plot(y=data$SWOLF_PhotochemicalSmog.BU0,x=data$SWOLF_PhotochemicalSmog.BU1,type='p',asp = 1)
lines(x=data$SWOLF_PhotochemicalSmog.BU1,y=data$SWOLF_PhotochemicalSmog.BU1,col="green")

plot(y=data$SWOLF_CED.BU0,x=data$SWOLF_CED.BU1,type='p',asp = 1)
lines(x=data$SWOLF_CED.BU1,y=data$SWOLF_CED.BU1,col="green")


data$BU1_IPCC_better <- ifelse( data$SWOLF_IPCC.BU0 >= data$SWOLF_IPCC.BU1,1,0)
data$BU1_Acidification_better <- ifelse( data$SWOLF_Acidification.BU0 >= data$SWOLF_Acidification.BU1,1,0)
data$BU1_Eutrophication_better <- ifelse( data$SWOLF_Eutrophication.BU0 >= data$SWOLF_Eutrophication.BU1,1,0)
data$BU1_Smog_better <- ifelse( data$SWOLF_PhotochemicalSmog.BU0 >= data$SWOLF_PhotochemicalSmog.BU1,1,0)
data$BU1_CED_better <- ifelse( data$SWOLF_CED.BU0 >= data$SWOLF_CED.BU1,1,0)


data$dif_IPCC_01 <- data$SWOLF_IPCC.BU1 - data$SWOLF_IPCC.BU0
plot(y=data$dif_IPCC_01,x=data$Lanfill.percCStor_LF,ylab = 'GWP of BU1 - GWP of BU0',
     main = 'Relation between the carbon storage and \n difference in GWP')
B <-cor(data$dif_IPCC_01,data)

data$dif_Acidification_01 <- data$SWOLF_Acidification.BU1 - data$SWOLF_Acidification.BU0
B <-cor(data$dif_Acidification_01,data)
plot(y=data$dif_Acidification_01,x=data$Land_app.perNasNH3fc * data$Land_app.perNH3evap,ylab = 'Acidification of BU1 - Acidification of BU0')

plot(y=data$SWOLF_IPCC.BU1,x=data$Soil_seq.perCStor)



### Calculating the emissions
N2O=1000*(1-data$Material_Properties.mcFC)*data$initflow.N_cont*(data$Land_app.perN2Oevap-data$Land_app.fert_N2O*data$Land_app.MFEN)/100*
      (2 * 14.007 + 15.999)/14.007/2*298

CStore = -1000*(1-data$Material_Properties.mcFC)*data$initflow.C_cont*(data$Soil_seq.perCStor/100) *
        (15.999 * 2 +12.011)/12.011

CStore_LF = -1000*(1-data$Material_Properties.mcFC)*data$initflow.C_cont*(data$Lanfill.percCStor_LF/100) *
            (15.999 * 2 +12.011)/12.011

Peat =- 1000 / data$Material_Properties.densFC * data$Land_app.densPeat/1000 * 25.18 

Nfert = -1000*(1-data$Material_Properties.mcFC)*data$initflow.N_cont*data$Land_app.MFEN * 12.69

Kfert = -1000*(1-data$Material_Properties.mcFC)*data$initflow.K_cont*data$Land_app.MFEK * 1

Pfert = -1000*(1-data$Material_Properties.mcFC)*data$initflow.P_cont*data$Land_app.MFEP * 0.49

Diesel = (0.8 - 1000*(1-data$Material_Properties.mcFC)* (data$initflow.N_cont*data$Land_app.MFEN*0.00229 +
         data$initflow.P_cont*data$Land_app.MFEP*0.00186+data$initflow.K_cont*data$Land_app.MFEK*0.00125))*3.544

C_CH4_Emitted = 1000*(1-data$Material_Properties.mcFC)*data$initflow.C_cont*(1-data$Lanfill.percCStor_LF/100) * 
                (4 +12.011)/12.011 /2 * (1-data$Lanfill.CH4_Collected/100) * (1-data$Lanfill.Frac_oxidized)* 25

C_CH4_Electricity = -1000*(1-data$Material_Properties.mcFC)*data$initflow.C_cont*(1-data$Lanfill.percCStor_LF/100)*
                    (4 +12.011)/12.011 /2 * data$Lanfill.CH4_Collected/100 * (1-data$Lanfill.Frac_flared)*50/3.6*0.36*0.76

plot(ecdf(C_CH4_Electricity))
hist(C_CH4_Emitted + C_CH4_Electricity , xlab = 'GWP')
hist( C_CH4_Electricity, xlab = 'GWP')
hist(C_CH4_Emitted, xlab = 'GWP')
hist(CStore_LF, xlab = 'GWP')

hist(N2O, xlab = 'GWP')
hist(CStore, xlab = 'GWP')
hist(N2O+CStore+Peat+Nfert+Kfert+Pfert, xlab = 'GWP')
hist(Diesel, xlab = 'GWP')
hist(Peat+Nfert+Kfert+Pfert+Diesel, xlab = 'GWP')

par(mfcol=c(2,1))
hist(C_CH4_Emitted + C_CH4_Electricity + CStore_LF, xlab = 'GWP',xlim = c(-1000,500))
hist(N2O+CStore+Peat+Nfert+Kfert+Pfert+Diesel, xlab = 'GWP',xlim = c(-1000,500))

### Checking that calculations fine in brightway2
fit = lm(data$SWOLF_IPCC.BU1~N2O+CStore+Peat+Nfert+Kfert+Pfert+Diesel)
summary(fit)
fit_1 = lm(data$SWOLF_IPCC.BU0~CStore_LF+C_CH4_Emitted + C_CH4_Electricity)
summary(fit_1)


### Histogram of difference in GWP
par(mfrow=c(2,2))
hist(x = data$SWOLF_IPCC.BU1, main = 'GWP of land applying compost', 
                              xlab = 'GWP include offset for peat + fertilizer',
                              xlim = c(-1200,600),
                              ylim = c(0,30000))

hist(x = data$SWOLF_IPCC.BU0, main = 'GWP of landfilling compost', 
     xlab = 'GWP',
     xlim = c(-1200,600),
     ylim = c(0,30000))

hist(x = data$SWOLF_IPCC.BU0-data$SWOLF_IPCC.BU1, main = 'Difference between the GWP of \n landfilling & land applying the compost', 
     xlab = 'GWP',
     xlim = c(-1200,600),
     ylim = c(0,20000),
     breaks = c(seq(-1300,1000,100)),
     col = c(rep('red',12),rep('blue',2),rep('green',9)))
legend('topleft',legend=c("Landfilling is better","Tie performance","Land applying is better"),
       bty = "n",pch =c(15, 15, 15),
       col=c("red","blue","green"))

data$hist_dif_GWP <- ifelse( data$SWOLF_IPCC.BU0-data$SWOLF_IPCC.BU1 <=-100 ,"Landfilling is better",ifelse( data$SWOLF_IPCC.BU0-data$SWOLF_IPCC.BU1 <=100 ,"Tie performance","Land applying is better"))
table(data$hist_dif_GWP)
barplot(sort(table(data$hist_dif_GWP)/1000,decreasing = T), ylim = c(0,100),
        col=c("red","blue","green"),
        ylab = 'Percent')
legend('topright',legend=c("Landfilling is better","Tie performance","Land applying is better"),
       bty = "n",pch =c(15, 15, 15),
       col=c("red","blue","green"))


### Histogram of difference in Acidification
par(mfrow=c(2,2))
hist(x = data$SWOLF_Acidification.BU1, main = 'Acidification of land applying compost', 
     xlab = 'Acidification include offset for peat + fertilizer',
     xlim = c(-5,5),
     ylim = c(0,35000))

hist(x = data$SWOLF_Acidification.BU0, main = 'Acidification of landfilling compost', 
     xlab = 'Acidification',
     xlim = c(-5,5),
     ylim = c(0,35000))

hist(x = data$SWOLF_Acidification.BU0-data$SWOLF_Acidification.BU1, main = 'Difference between the Acidification of \n landfilling & land applying the compost', 
     xlab = 'Acidification',
     xlim = c(-5,5),
     ylim = c(0,70000),
     breaks = c(seq(-7,5,1)),
     col = c(rep('red',6),rep('blue',2),rep('green',4)))
legend('topleft',legend=c("Landfilling is better","Tie performance","Land applying is better"),
       bty = "n",pch =c(15, 15, 15),
       col=c("red","blue","green"))

data$hist_dif_acid <- ifelse( data$SWOLF_Acidification.BU0-data$SWOLF_Acidification.BU1 <=-1 ,"Landfilling is better",ifelse( data$SWOLF_Acidification.BU0-data$SWOLF_Acidification.BU1 <=1 ,"Tie performance","Land applying is better"))
table(data$hist_dif_acid)
barplot(sort(table(data$hist_dif_acid)/1000,decreasing = T), ylim = c(0,100),
        col=c("blue","red","green"),
        ylab = 'Percent')
legend('topright',legend=c("Tie performance","Landfilling is better","Land applying is better"),
       bty = "n",pch =c(15, 15, 15),
       col=c("blue","red","green"))




### Histogram of difference in Eutrophication
par(mfrow=c(2,2))
hist(x = data$SWOLF_Eutrophication.BU1, main = 'Eutrophication of land applying compost', 
     xlab = 'Eutrophication include offset for peat + fertilizer',
     xlim = c(-5,20),
     ylim = c(0,30000))

hist(x = data$SWOLF_Eutrophication.BU0, main = 'Eutrophication of landfilling compost', 
     xlab = 'Eutrophication',
     xlim = c(-5,20),
     ylim = c(0,30000))

hist(x = data$SWOLF_Eutrophication.BU0-data$SWOLF_Eutrophication.BU1, main = 'Difference between the Eutrophication of \n landfilling & land applying the compost', 
     xlab = 'Eutrophication',
     xlim = c(-20,10),
     ylim = c(0,45000),
     breaks = c(seq(-20,10,2)),
     col = c(rep('red',9),rep('blue',2),rep('green',4)))

legend('topleft',legend=c("Landfilling is better","Tie performance","Land applying is better"),
       bty = "n",pch =c(15, 15, 15),
       col=c("red","blue","green"))

data$hist_dif_Eutr <- ifelse( data$SWOLF_Eutrophication.BU0-data$SWOLF_Eutrophication.BU1 <=-1 ,"Landfilling is better",ifelse( data$SWOLF_Eutrophication.BU0-data$SWOLF_Eutrophication.BU1 <=1 ,"Tie performance","Land applying is better"))
table(data$hist_dif_Eutr)
barplot(sort(table(data$hist_dif_Eutr)/1000,decreasing = T), ylim = c(0,100),
        col=c("red","blue","green"),
        ylab = 'Percent')
legend('topright',legend=c("Landfilling is better","Tie performance","Land applying is better"),
       bty = "n",pch =c(15, 15, 15),
       col=c("red","blue","green"))

### Histogram of difference in Smog
par(mfrow=c(2,2))
hist(x = data$SWOLF_PhotochemicalSmog.BU1, main = 'Smog of land applying compost', 
     xlab = 'Smog include offset for peat + fertilizer',
     xlim = c(-20,5),
     ylim = c(0,25000))

hist(x = data$SWOLF_PhotochemicalSmog.BU0, main = 'Smog of landfilling compost', 
     xlab = 'Smog',
     xlim = c(-20,5),
     ylim = c(0,25000))

hist(x = data$SWOLF_PhotochemicalSmog.BU0-data$SWOLF_PhotochemicalSmog.BU1, main = 'Difference between the Smog of \n landfilling & land applying the compost', 
     xlab = 'Smog',
     xlim = c(-5,25),
     ylim = c(0,30000),
     breaks = c(seq(-10,26,2)),
     col = c(rep('red',4),rep('blue',2),rep('green',12)))

legend('topright',legend=c("Landfilling is better","Tie performance","Land applying is better"),
       bty = "n",pch =c(15, 15, 15),
       col=c("red","blue","green"))

data$hist_dif_smog <- ifelse( data$SWOLF_PhotochemicalSmog.BU0-data$SWOLF_PhotochemicalSmog.BU1 <=-1 ,"Landfilling is better",ifelse( data$SWOLF_PhotochemicalSmog.BU0-data$SWOLF_PhotochemicalSmog.BU1 <=1 ,"Tie performance","Land applying is better"))
table(data$hist_dif_smog)
barplot(sort(table(data$hist_dif_smog)/1000,decreasing = T), ylim = c(0,100),
        col=c("green","blue","red"),
        ylab = 'Percent')
legend('topright',legend=c("Land applying is better","Tie performance","Landfilling is better"),
       bty = "n",pch =c(15, 15, 15),
       col=c("green","blue","red"))




### Corrolation for difference in results
x=data.frame(N2O,CStore,CStore_LF,Peat,Nfert,Kfert,Pfert,Diesel,C_CH4_Emitted,C_CH4_Electricity)
data.cor = data[21:45]
data.cor$dif_gwp = data$SWOLF_IPCC.BU0 - data$SWOLF_IPCC.BU1
x$dif_gwp = data$SWOLF_IPCC.BU0 - data$SWOLF_IPCC.BU1
A=cor(x)
#install.packages('corrplot')
library(corrplot)
par(mfrow=c(1,1))
corrplot(A, method = "number", type = "upper",font=2)

###############

### Rank analysis:
par(mfrow=c(1,1))
p1=hist(x = data$SWOLF_IPCC.BU1)
p2=hist(x = data$SWOLF_IPCC.BU0)

plot(p1, col = rgb(0,1,0,0.4), ylim = c(0,30000),
     xlim = c(-1200,600), main = 'GWP of compost final use', 
     xlab = 'GWP')
plot(p2,col = rgb(1,0,0,0.4),add=T)
legend('topright',legend=c("Landfilling","Land applying"),
       bty = "n",pch =c(15, 15),
       col=c(rgb(1,0,0,0.4),rgb(0,1,0,0.4)))

tes = cor(data.cor,method = 'spearman')




