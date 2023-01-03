import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl

marks = ctrl.Antecedent(np.arange(0, 101, 1), 'marks')
attendance = ctrl.Antecedent(np.arange(0, 101, 1), 'attendance')
score = ctrl.Consequent(np.arange(0, 11, 1), 'score')

marks.automf(5)
attendance.automf(5)
score.automf(5)

rule1 = ctrl.Rule(marks['poor'] & attendance['poor'], score['poor'])
rule2 = ctrl.Rule(marks['poor'] & attendance['mediocre'], score['poor'])
rule3 = ctrl.Rule(marks['poor'] & attendance['average'], score['mediocre'])
rule4 = ctrl.Rule(marks['poor'] & attendance['decent'], score['mediocre'])
rule5 = ctrl.Rule(marks['poor'] & attendance['good'], score['mediocre'])
rule6 = ctrl.Rule(marks['mediocre'] & attendance['poor'], score['mediocre'])
rule7 = ctrl.Rule(marks['mediocre'] & attendance['mediocre'], score['mediocre'])
rule8 = ctrl.Rule(marks['mediocre'] & attendance['average'], score['mediocre'])
rule9 = ctrl.Rule(marks['mediocre'] & attendance['decent'], score['mediocre'])
rule10 = ctrl.Rule(marks['mediocre'] & attendance['good'], score['average'])
rule11 = ctrl.Rule(marks['average'] & attendance['poor'], score['mediocre'])
rule12 = ctrl.Rule(marks['average'] & attendance['mediocre'], score['average'])
rule13 = ctrl.Rule(marks['average'] & attendance['average'], score['average'])
rule14 = ctrl.Rule(marks['average'] & attendance['decent'], score['decent'])
rule15 = ctrl.Rule(marks['average'] & attendance['good'], score['decent'])
rule16 = ctrl.Rule(marks['decent'] & attendance['poor'], score['average'])
rule17 = ctrl.Rule(marks['decent'] & attendance['mediocre'], score['average'])
rule18 = ctrl.Rule(marks['decent'] & attendance['average'], score['decent'])
rule19 = ctrl.Rule(marks['decent'] & attendance['decent'], score['decent'])
rule20 = ctrl.Rule(marks['decent'] & attendance['good'], score['good'])
rule21 = ctrl.Rule(marks['good'] & attendance['poor'], score['average'])
rule22 = ctrl.Rule(marks['good'] & attendance['mediocre'], score['decent'])
rule23 = ctrl.Rule(marks['good'] & attendance['average'], score['decent'])
rule24 = ctrl.Rule(marks['good'] & attendance['decent'], score['good'])
rule25 = ctrl.Rule(marks['good'] & attendance['good'], score['good'])

score_ctrl = ctrl.ControlSystem(
    [rule1, rule2, rule3, rule4, rule5, rule6, rule7, rule8, rule9, rule10, 
     rule11, rule12, rule13, rule14, rule15, rule16, rule17, rule18, rule19, rule20, 
     rule21, rule22, rule23, rule24, rule25
    ]
    )

scoring = ctrl.ControlSystemSimulation(score_ctrl)

#scoring.input['marks'] = m
#scoring.input['attendance'] = a

#scoring.compute()

#print(scoring.output['score'])

def enter_details(m,a):
    scoring.input['marks'] = m
    scoring.input['attendance'] = a
    scoring.compute()
    return scoring.output['score']
