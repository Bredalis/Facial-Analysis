
import cv2

# Capturar video desde la cámara
cap = cv2.VideoCapture(0)

# Definir el codec y crear el objeto VideoWriter
fourcc = cv2.VideoWriter_fourcc(*"XVID")
out = cv2.VideoWriter(
	"Facial_Expressions.avi", fourcc, 
	20.0, (640, 480)
)

while cap.isOpened():
	ret, frame = cap.read()

	# Si no se pudo leer el frame
	if not ret:
		break

	# Guardar el frame en el video
	out.write(frame)

	# Mostrar el video en pantalla
	cv2.imshow("Grabando video...", frame)

	# Detectar tecla para salir
	if cv2.waitKey(1) & 0xFF == ord("q"):
		break

# Liberar recursos (cerrar cámara, archivo de video y ventanas)
cap.release()
out.release()
cv2.destroyAllWindows()