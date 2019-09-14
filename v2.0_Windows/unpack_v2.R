args = commandArgs(trailingOnly=TRUE)

if (length(args)<2) {
  stop("At least two arguments must be supplied.\n", call.=FALSE)
} 

# args[1] should be the directory path
path <- args[1]

# output adds desired output name; should end in .txt for text file
output <- paste(path,"\\matrix_file_nr.txt",sep="")

# set up database access/library calls/driver
# args[2] should be the name of the .db file
database <- paste(path,args[2],sep="\\")
library("DBI")
library("RSQLite")
driver <- dbDriver("SQLite",max.con = 25)
con <- dbConnect(driver, dbname=database)



# create matrices; separated by data type (one is numbers, two is strings, three is numbers)
matrix.one <- data.matrix(dbGetQuery(con,paste("select cohortID, year from cohorts")))
matrix.two <- as.matrix(dbGetQuery(con,paste("select species from cohorts")))
matrix.three <- data.matrix(dbGetQuery(con,paste("select trees, diameter, height from cohorts")))

# create dataframe to preserve data types for output
end.matrix <- data.frame(matrix.one,matrix.two,matrix.three)

# output dataframe to txt file
write.table(end.matrix, file = output, append = FALSE, sep = " ", row.names = FALSE, col.names = FALSE)

# close database connection
dbDisconnect(con)