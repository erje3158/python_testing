quad <- read.csv('quad.csv')
print('The following is the contents of the quad.csv standard file:')
print(quad)
jpeg("quad.jpg")
plot(quad, type='o', main="Quadratic Curve: y = x^2")
dev.off()

