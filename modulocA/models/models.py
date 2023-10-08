#Author - Abril Jimenez Alatriste 
from odoo import api, fields, models

class Profesor(models.Model):
    _name = 'moduloCA.profesor'
    _description = 'Modelo de Profesor para moduloCA'
    
    name = fields.Char(string='Nombre del Profesor')
    especialidad = fields.Char(string='Especialidad')
    clases_ids = fields.One2many('moduloCA.clase', 'profesor_id', string='Clases Impartidas')

class Clase(models.Model):
    _name = 'moduloCA.clase'
    _description = 'Modelo de Clase para moduloCA'
    
    name = fields.Char(string='Nombre de la Clase')
    cupo = fields.Integer(string='Cupo Máximo', help='Número máximo de personas que pueden inscribirse en la clase')
    profesor_id = fields.Many2one('moduloCA.profesor', string='Profesor que Imparte')
    salon_id = fields.Many2one('moduloCA.salon', string='Salón Asignado')
    feedback_ids = fields.One2many('moduloCA.feedback', 'clase_id', string='Feedbacks de la Clase')

class Salon(models.Model):
    _name = 'moduloCA.salon'
    _description = 'Modelo de Salón para moduloCA'
    
    name = fields.Char(string='Nombre del Salón')
    capacidad = fields.Integer(string='Capacidad')
    clases_ids = fields.One2many('moduloCA.clase', 'salon_id', string='Clases en el Salón')

class Horario(models.Model):
    _name = 'moduloCA.horario'
    _description = 'Modelo de Horario para moduloCA'
    
    hora_inicio = fields.Datetime(string='Hora de Inicio')
    hora_fin = fields.Datetime(string='Hora de Fin')
    clase_id = fields.Many2one('moduloCA.clase', string='Clase Asociada')
    dia = fields.Selection([
        ('lunes', 'Lunes'),
        ('martes', 'Martes'),
        ('miercoles', 'Miércoles'),
        ('jueves', 'Jueves'),
        ('viernes', 'Viernes'),
        ('sabado', 'Sábado'),
        ('domingo', 'Domingo'),
    ], string='Día de la Semana')

class Feedback(models.Model):
    _name = 'moduloCA.feedback'
    _description = 'Modelo de Feedback para moduloCA'
    
    comentario = fields.Text(string='Comentario del Estudiante')
    rating = fields.Selection([
        ('1', 'Malo'),
        ('2', 'Regular'),
        ('3', 'Bueno'),
        ('4', 'Muy bueno'),
        ('5', 'Excelente'),
    ], string='Rating de la Clase')
    clase_id = fields.Many2one('moduloCA.clase', string='Clase Asociada')
