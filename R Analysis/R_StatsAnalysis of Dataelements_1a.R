#Step-#Import dependency
library(tidyverse)
?mutate()
?ggplot()
?shapiro.test()

#Step-#Import and read in the
North_Data_Finalized_c02ch4<-read.csv(file='North_Data_Finalized_co2ch4',check.names = F,stringsAsFactors = F)

North_Data_Finalized_c02ch4<-read.table.url(url(description = "https://github.com/ALIYA2Group/Mod20_Segment_2/blob/main/ETL%20Data/North_Data_Finalized_co2ch4.csv"), method="auto",...)
#scan.url(url, method="auto", ...)
#source.url(url, method="auto", ...)

#Step=#Mean, Min, Max
summarize_temp2m <- North_Data_Finalized_1 %>% summarize(Mean_temp2m=mean(temperature_2m),Max_temp2m=max(temperature_2m),Min_temp2m=min(temperature_2m), .groups = 'keep') #create summary table with multiple columns
summarize_siconc <- North_Data_Finalized_1 %>% summarize(Mean_siconc=mean(siconc),Max_siconc=max(siconc),Min_siconc=min(siconc), .groups = 'keep') #create summary table with multiple columns
summarize_Snow_albedo <- North_Data_Finalized_1 %>% summarize(Mean_Snow_albedo=mean(Snow_albedo),Max_Snow_albedo=max(Snow_albedo),Min_Snow_albedo=min(Snow_albedo), .groups = 'keep') #create summary table with multiple columns
summarize_snow_melt <- North_Data_Finalized_1 %>% summarize(Mean_snow_melt=mean(snow_melt),Max_snow_melt=max(snow_melt),Min_snow_melt=min(snow_melt), .groups = 'keep') #create summary table with multiple columns
summarize_surface_pressure <- North_Data_Finalized_1 %>% summarize(Mean_surface_pressure=mean(surface_pressure),Max_surface_pressure=max(surface_pressure),Min_surface_pressure=min(surface_pressure), .groups = 'keep') #create summary table with multiple columns
summarize_Total_column_ozone <- North_Data_Finalized_1 %>% summarize(Mean_Total_column_ozone=mean(Total_column_ozone),Max_Total_column_ozonet=max(Total_column_ozone),Min_Total_column_ozone=min(Total_column_ozone), .groups = 'keep') #create summary table with multiple columns
summarize_Extent <- North_Data_Finalized_1 %>% summarize(Mean_Extent=mean(Extent),Max_Total_Extent=max(Extent),Min_Total_Extent=min(Extent), .groups = 'keep') #create summary table with multiple columns
summarize_xco2 <- North_Data_Finalized_1 %>% summarize(Mean_xco2=mean(xco2),Max_xco2=max(xco2),Min_xco2=min(xco2), .groups = 'keep') #create summary table with multiple columns
summarize_xch4 <- North_Data_Finalized_1 %>% summarize(Mean_xch4=mean(xch4),Max_xch42=max(xch4),Min_xch4=min(xch4), .groups = 'keep') #create summary table with multiple columns
> #Step=Bar Graph

plt <- ggplot(North_Data_Finalized2,aes(x=time, y=snow_melt))
plt + geom_col() 

plt <- ggplot(North_Data_Finalized2,aes(x=time, y=siconc))
plt + geom_col()

plt <- ggplot(North_Data_Finalized2,aes(x=time, y=Total_column_ozone))
plt + geom_col()

plt <- ggplot(North_Data_Finalized2,aes(x=time, y=Extent))
plt + geom_col()

#Step Other Graph needed scatter

plt <- ggplot(North_Data_Finalized2,aes(x=time, y=surface_pressure))
plt + geom_point(size=4) + labs(x="time",y="surface_pressure")
plt <- ggplot(North_Data_Finalized2,aes(x=time, y=temperature_2m))
plt + geom_point(size=4) + labs(x="time",y="temperature_2m")
plt <- ggplot(North_Data_Finalized2,aes(x=time, y=Snow_albedo))
plt + geom_point(size=4) + labs(x="time",y="Snow_albedo")
#step to 
plt <- ggplot(North_Data_Finalized2,aes(x=time, y=xco2))
plt + geom_col()

plt <- ggplot(North_Data_Finalized2,aes(x=time, y=xch4))
plt + geom_col()


# Scatter graph t-test
> #t.test surface_pressure n Snow_albedo
t.test(North_Data_Finalized2$surface_pressure,North_Data_Finalized2$Snow_albedo)
> #t.test temperature_2m n Snow_albedo
t.test(North_Data_Finalized2$temperature_2m,North_Data_Finalized2$Snow_albedo)
> #t.test surface_pressure n Snow_albedo
t.test(North_Data_Finalized2$temperature_2m,North_Data_Finalized2$surface_pressure)

> siconc

t.test(North_Data_Finalized2$siconc,North_Data_Finalized2$snow_melt)
t.test(North_Data_Finalized2$siconc,North_Data_Finalized2$Total_column_ozone)
t.test(North_Data_Finalized2$siconc,North_Data_Finalized2$Extent)

> snow_melt,
t.test(North_Data_Finalized2$siconc,North_Data_Finalized2$snow_melt)
t.test(North_Data_Finalized2$snow_melt,North_Data_Finalized2$Total_column_ozone)
t.test(North_Data_Finalized2$snow_melt,North_Data_Finalized2$Extent)

> Total_column_ozone

t.test(North_Data_Finalized2$Total_column_ozone,North_Data_Finalized2$snow_melt)
t.test(North_Data_Finalized2$siconc,North_Data_Finalized2$Total_column_ozone)
t.test(North_Data_Finalized2$Total_column_ozone,North_Data_Finalized2$Extent)

> Extent
t.test(North_Data_Finalized2$siconc,North_Data_Finalized2$snow_melt)
t.test(North_Data_Finalized2$siconc,North_Data_Finalized2$Total_column_ozone)
t.test(North_Data_Finalized2$siconc,North_Data_Finalized2$Extent)