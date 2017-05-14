adding <- function(num1,num2){
    num1 + num2
}
adding(45,72)


subtracting <- function(num1,num2){
  num1 - num2
}
subtracting(45,2)


multiplying <- function(num1,num2){
  num1 * num2
}
multiplying(3,8)


dividing <- function(num1,num2){
  if (num2==0) {
    my_result <- "undefined" 
  } else {
    my_result <- (num1/num2)
  }
  return(my_result)
}
dividing(4,2)


sq_rooting <- function(num1){
  if (num1 < 0) {
    my_result <- "undefined" 
  } else {
    my_result <- sqrt(num1)
  }
  return(my_result)
}
sq_rooting(4)


exponentiating <- function(num1,num2){
  num1^num2
}
exponentiating(3,2)


squaring <- function(num1){
  num1*num1
}
squaring(8)


cubing <- function(num1){
  num1*num1*num1
}
cubing(8)


#takes input in degrees
sineing <- function(num1){
  sin(num1*pi/180)
}
sineing(90)


#takes input in degrees
cosineing <- function(num1){
  cos(num1*pi/180)
}
sineing(180)
