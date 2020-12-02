mydataset = read.csv('mydata.csv')

mydataset$Age = ifelse(is.na(mydataset$Age),ave(mydataset$Age, FUN = function(x)
  mean(x,na.rm =TRUE)),
  mydataset$Age)

mydataset$Income = ifelse(is.na(mydataset$Income),ave(mydataset$Income, FUN = function(x)
  mean(x,na.rm =TRUE)),
  mydataset$Income)

  # added
  