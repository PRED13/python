from MiniLangVisitor import MiniLangVisitor

class MiniLangVisitorImpl(MiniLangVisitor):
    def __init__(self):
        self.memory = {}

    def visitAssign(self, ctx):
        id_ = ctx.ID().getText()
        value = self.visit(ctx.expr())
        self.memory[id_] = value
        return value

    def visitPrint(self, ctx):
        value = self.visit(ctx.expr())
        print(value)
        return value

    def visitFromStmt(self, ctx):
        module_name = ctx.ID(0).getText()
        var_name = ctx.ID(1).getText()
        print(f"Importando '{var_name}' desde el módulo '{module_name}'")
        # Simula una importación
        self.memory[var_name] = f"{module_name}.{var_name}"
        return self.memory[var_name]

    def visitExpr(self, ctx):
        if ctx.INT():
            return int(ctx.INT().getText())
        elif ctx.ID():
            name = ctx.ID().getText()
            return self.memory.get(name, 0)
        elif ctx.op:
            left = self.visit(ctx.expr(0))
            right = self.visit(ctx.expr(1))
            op = ctx.op.text
            if op == '+': return left + right
            if op == '-': return left - right
            if op == '*': return left * right
            if op == '/': return left / right
        else:
            return self.visit(ctx.expr(0))
