from django.db import models

# Create your models here.

from django.db import models


class Usuario(models.Model):
    ROLES = [
        ('ESTUDIANTE', 'Estudiante'),
        ('INSTRUCTOR', 'Instructor'),
        ('ADMIN', 'Administrador'),
    ]

    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    rut = models.CharField(max_length=12, unique=True)
    username = models.CharField(max_length=50, unique=True)
    correo_institucional = models.EmailField(unique=True)
    telefono = models.CharField(max_length=15, blank=True, null=True)
    contrasenia = models.CharField(max_length=128)
    habilitado = models.BooleanField(default=True)
    rol_principal = models.CharField(max_length=15, choices=ROLES, default='ESTUDIANTE')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.nombre} {self.apellido} ({self.username})"


class HistorialConexion(models.Model):
    id_usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='conexiones')
    fechahora_ingreso = models.DateTimeField(auto_now_add=True)
    fechahora_salida = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"Sesión de {self.id_usuario.username} iniciada el {self.fechahora_ingreso}"


class Curso(models.Model):
    ESTADOS_CURSO = [
        ('BORRADOR', 'Borrador'),
        ('PUBLICADO', 'Publicado'),
        ('EN_CURSO', 'En Curso'),
        ('FINALIZADO', 'Finalizado'),
        ('ARCHIVADO', 'Archivado'),
    ]

    id_instructor = models.ForeignKey(Usuario, on_delete=models.PROTECT, related_name='cursos_impartidos')
    codigo = models.CharField(max_length=20)
    periodo = models.CharField(max_length=15)
    titulo = models.CharField(max_length=150)
    descripcion = models.TextField()
    estado = models.CharField(max_length=15, choices=ESTADOS_CURSO, default='BORRADOR')
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['codigo', 'periodo'], name='unique_curso_periodo')
        ]

    def __str__(self):
        return f"{self.codigo} ({self.periodo}) - {self.titulo}"


class Seccion(models.Model):
    id_curso = models.ForeignKey(Curso, on_delete=models.CASCADE, related_name='secciones')
    titulo = models.CharField(max_length=150)
    orden = models.PositiveSmallIntegerField(default=1)
    descripcion = models.TextField(blank=True, null=True)
    visibilidad = models.BooleanField(default=True)

    class Meta:
        ordering = ['orden']

    def __str__(self):
        return f"{self.id_curso.codigo} - Sec {self.orden}: {self.titulo}"


class Leccion(models.Model):
    TIPOS_LECCION = [
        ('TEXTO', 'Texto / Lectura'),
        ('VIDEO', 'Video'),
        ('ARCHIVO', 'Documento / Archivo descargable'),
    ]

    id_seccion = models.ForeignKey(Seccion, on_delete=models.CASCADE, related_name='lecciones')
    titulo = models.CharField(max_length=150)
    orden = models.PositiveSmallIntegerField(default=1)
    contenido_texto = models.TextField(blank=True, null=True)
    tipo = models.CharField(max_length=10, choices=TIPOS_LECCION, default='TEXTO')
    url = models.URLField(max_length=255, blank=True, null=True)
    archivo = models.FileField(upload_to='lecciones_archivos/', blank=True, null=True)
    visibilidad = models.BooleanField(default=True)

    class Meta:
        ordering = ['orden']

    def __str__(self):
        return f"Lección {self.orden}: {self.titulo}"


class Evaluacion(models.Model):
    ESTADOS_EVALUACION = [
        ('BORRADOR', 'Borrador'),
        ('DISPONIBLE', 'Disponible'),
        ('CERRADA', 'Cerrada'),
    ]

    id_seccion = models.ForeignKey(Seccion, on_delete=models.CASCADE, related_name='evaluaciones')
    titulo = models.CharField(max_length=150)
    descripcion = models.TextField(blank=True, null=True)
    estado = models.CharField(max_length=15, choices=ESTADOS_EVALUACION, default='BORRADOR')
    visibilidad = models.BooleanField(default=True)
    fecha_inicio = models.DateTimeField()
    fecha_limite = models.DateTimeField()
    puntaje_maximo = models.DecimalField(max_digits=5, decimal_places=2, default=100.00)

    def __str__(self):
        return f"Evaluación: {self.titulo}"


class Pregunta(models.Model):
    TIPOS_PREGUNTA = [
        ('MULTIPLE', 'Selección Múltiple'),
        ('VERDADERO_FALSO', 'Verdadero o Falso'),
        ('ABIERTA', 'Desarrollo / Abierta'),
    ]

    id_evaluacion = models.ForeignKey(Evaluacion, on_delete=models.CASCADE, related_name='preguntas')
    enunciado = models.TextField()
    tipo_pregunta = models.CharField(max_length=20, choices=TIPOS_PREGUNTA, default='MULTIPLE')
    puntaje = models.DecimalField(max_digits=4, decimal_places=2, default=1.00)

    def __str__(self):
        return f"{self.enunciado[:50]}... ({self.puntaje} pts)"


class Opcion(models.Model):
    id_pregunta = models.ForeignKey(Pregunta, on_delete=models.CASCADE, related_name='opciones')
    texto = models.CharField(max_length=255)
    es_correcta = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.texto} ({'Correcta' if self.es_correcta else 'Incorrecta'})"


class Matricula(models.Model):
    ESTADOS_MATRICULA = [
        ('ACTIVA', 'Activa'),
        ('CONGELADA', 'Congelada'),
        ('FINALIZADA', 'Finalizada'),
        ('CANCELADA', 'Cancelada'),
    ]

    id_estudiante = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='matriculas')
    id_curso = models.ForeignKey(Curso, on_delete=models.CASCADE, related_name='alumnos_matriculados')
    estado = models.CharField(max_length=15, choices=ESTADOS_MATRICULA, default='ACTIVA')
    nota_final = models.DecimalField(max_digits=3, decimal_places=1, null=True, blank=True)
    fecha_inscripcion = models.DateTimeField(auto_now_add=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['id_estudiante', 'id_curso'], name='unique_matricula_estudiante_curso')
        ]

    def __str__(self):
        return f"{self.id_estudiante.username} en {self.id_curso.codigo}"


class ProgresoLeccion(models.Model):
    id_matricula = models.ForeignKey(Matricula, on_delete=models.CASCADE, related_name='progresos_lecciones')
    id_leccion = models.ForeignKey(Leccion, on_delete=models.CASCADE, related_name='progresos')
    fecha_completado = models.DateTimeField(null=True, blank=True)
    completada = models.BooleanField(default=False)
    cantidad_accesos = models.PositiveIntegerField(default=0)
    ultimo_acceso = models.DateTimeField(null=True, blank=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['id_matricula', 'id_leccion'], name='unique_progreso_leccion')
        ]


class EntregaEvaluacion(models.Model):
    ESTADOS_CALIFICACION = [
        ('PENDIENTE', 'Pendiente'),
        ('CALIFICADA', 'Calificada'),
        ('CORREGIDA_MANUAL', 'Corregida Manualmente'),
    ]

    id_evaluacion = models.ForeignKey(Evaluacion, on_delete=models.CASCADE, related_name='entregas')
    id_matricula = models.ForeignKey(Matricula, on_delete=models.CASCADE, related_name='evaluaciones_entregadas')
    estado_calificacion = models.CharField(max_length=20, choices=ESTADOS_CALIFICACION, default='PENDIENTE')
    nota = models.DecimalField(max_digits=3, decimal_places=1, null=True, blank=True)
    aprobado = models.BooleanField(default=False)
    fecha_entrega = models.DateTimeField(auto_now_add=True)
    numero_intento = models.PositiveSmallIntegerField(default=1)

    def __str__(self):
        return f"Entrega #{self.numero_intento} - {self.id_matricula.id_estudiante.username} ({self.id_evaluacion.titulo})"


class RespuestaEstudiante(models.Model):
    id_entrega_evaluacion = models.ForeignKey(EntregaEvaluacion, on_delete=models.CASCADE, related_name='respuestas')
    id_pregunta = models.ForeignKey(Pregunta, on_delete=models.CASCADE, related_name='respuestas_alumnos')
    id_opcion = models.ForeignKey(Opcion, on_delete=models.SET_NULL, null=True, blank=True, related_name='respuestas_seleccionadas')
    texto_abierto = models.TextField(blank=True, null=True)
    retroalimentacion = models.TextField(blank=True, null=True)
    puntaje_obtenido = models.DecimalField(max_digits=4, decimal_places=2, default=0.00)


class RegistroAuditoria(models.Model):
    ACCIONES = [
        ('CREAR', 'Crear'),
        ('MODIFICAR', 'Modificar'),
        ('ELIMINAR', 'Eliminar'),
        ('CAMBIO_ESTADO', 'Cambio de Estado'),
    ]

    id_usuario = models.ForeignKey(Usuario, on_delete=models.SET_NULL, null=True, related_name='acciones_auditoria')
    accion = models.CharField(max_length=20, choices=ACCIONES)
    tabla_afectada = models.CharField(max_length=50)
    id_registro_modificado = models.PositiveIntegerField()
    estado_anterior = models.JSONField(blank=True, null=True)
    estado_nuevo = models.JSONField(blank=True, null=True)
    fecha_modificacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"[{self.accion}] en {self.tabla_afectada} por {self.id_usuario} ({self.fecha_modificacion})"


class Notificacion(models.Model):
    id_curso = models.ForeignKey(Curso, on_delete=models.CASCADE, null=True, blank=True, related_name='notificaciones')
    id_usuario_emisor = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='notificaciones_enviadas')
    id_usuario_receptor = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='notificaciones_recibidas')
    titulo = models.CharField(max_length=120)
    mensaje = models.CharField(max_length=255)
    fecha = models.DateTimeField(auto_now_add=True)
    leido = models.BooleanField(default=False)

    class Meta:
        ordering = ['-fecha']

    def __str__(self):
        return f"Notificación para {self.id_usuario_receptor.username}: {self.titulo}"