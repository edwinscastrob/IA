import tensorflow as tf

#escalar
entero =tf.Variable(5,tf.int32)
flotante=tf.Variable(3.1416,tf.float32)

#vector
cadena=tf.string_join(["hola","ab","cd"])
vectorEnteros=tf.Variable([1,2,3,4,5,6],tf.int64)

#matriz
matrizEnteros=tf.Variable([[1,2,3,4,5,6],[1,3,5,7,9]],tf.int64)

