from aima3 import logic

'''
If a man is married to a women and the man has a biological chield who is not the biological
child of the women and the woman has a biological chiled who is not the biological child
of the man, then the children are step brothers.
'''

#Part A
################################
clauses =[]

#Writing the first sentence in first order logic
clauses.append(logic.expr('''(Man(x) & Women(y) & Married(x, y) & BiologicalChield(xc, x) & BiologicalChield(yc, y)
 & NotBiologicalChield(xc, y) & NotBiologicalChield(yc, x)) ==> StepBrothers(xc, yc)'''))

#Just in case if there was a mix in the input like insted of putting the man first we put the women
#(Note: even if the two below lines were omitted the code will work because I did not mix)
#clauses.append(logic.expr("Married(y, x) ==> Married(x, y)"))
#clauses.append(logic.expr("StepBrothers(yc, xc) ==> StepBrothers(xc, yc)"))

#Adding the expressions
KB =logic.FolKB(clauses)
KB.tell(logic.expr('Man(Ahmad)'))
KB.tell(logic.expr('Women(Layla)'))
KB.tell(logic.expr('Married(Ahmad, Layla)'))
KB.tell(logic.expr('BiologicalChield(Hassan, Ahmad)'))
KB.tell(logic.expr('BiologicalChield(Mahmoud, Layla)'))
KB.tell(logic.expr('NotBiologicalChield(Hassan, Layla)'))
KB.tell(logic.expr('NotBiologicalChield(Mahmoud, Ahmad)'))

#Checking if we have step brother (Note: the arguments are dummy variables we could choose what ever we like) 
stepBrothers=logic.fol_fc_ask(KB,logic.expr("StepBrothers(dum_x,dum_y)"))

#Getting the result
print("Part A answare: "+str(list(stepBrothers)))

#Part B
################################
#By using the same logic as part A
KB.tell(logic.expr("BrotherOrStepBrother(xc, yc) & HasAson(xc,xcc) ==> Uncle(yc,xcc)"))

#Just in case if there is a mix in the input
clauses.append(logic.expr("BrotherOrStepBrother(yc, xc) ==> BrotherOrStepBrother(xc, yc)"))

KB.tell(logic.expr("BrotherOrStepBrother(Hassan, Mahmoud)"))
KB.tell(logic.expr("HasAson(Hassan, Ibrahim)"))
uncle=logic.fol_fc_ask(KB,logic.expr("Uncle(uncle, nephew)"))

uncle=list(uncle)

#Getting the result
print("Part B answare: "+str(list(uncle)))



