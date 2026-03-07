from src.ir import ast
from src.ir import types


class ASTVisitor():

    def result(self):
        raise NotImplementedError('result() must be implemented')

    def visit(self, node):
        visitors = {
            ast.SuperClassInstantiation: self.visit_super_instantiation,
            ast.ClassDeclaration: self.visit_class_decl,
            types.TypeParameter: self.visit_type_param,
            ast.CallArgument: self.visit_call_argument,
            ast.FieldDeclaration: self.visit_field_decl,
            ast.VariableDeclaration: self.visit_var_decl,
            ast.ParameterDeclaration: self.visit_param_decl,
            ast.FunctionDeclaration: self.visit_func_decl,
            ast.Lambda: self.visit_lambda,
            ast.FunctionReference: self.visit_func_ref,
            ast.BottomConstant: self.visit_bottom_constant,
            ast.IntegerConstant: self.visit_integer_constant,
            ast.RealConstant: self.visit_real_constant,
            ast.CharConstant: self.visit_char_constant,
            ast.StringConstant: self.visit_string_constant,
            ast.ArrayExpr: self.visit_array_expr,
            ast.BooleanConstant: self.visit_boolean_constant,
            ast.Variable: self.visit_variable,
            ast.LogicalExpr: self.visit_logical_expr,
            ast.EqualityExpr: self.visit_equality_expr,
            ast.ComparisonExpr: self.visit_comparison_expr,
            ast.ArithExpr: self.visit_arith_expr,
            ast.Conditional: self.visit_conditional,
            ast.Is: self.visit_is,
            ast.New: self.visit_new,
            ast.FieldAccess: self.visit_field_access,
            ast.FunctionCall: self.visit_func_call,
            ast.Assignment: self.visit_assign,
            ast.Program: self.visit_program,
            ast.Block: self.visit_block,
        }
        visitor = visitors.get(node.__class__)
        if visitor is None:
            raise Exception(
                "Cannot find visitor for instance node " + str(node.__class__))
        return visitor(node)

    def visit_program(self, node):
        raise NotImplementedError('visit_program() must be implemented')

    def visit_block(self, node):
        raise NotImplementedError('visit_block() must be implemented')

    def visit_super_instantiation(self, node):
        raise NotImplementedError(
            'visit_super_instantiation() must be implemented')

    def visit_class_decl(self, node):
        raise NotImplementedError('visit_class_decl() must be implemented')

    def visit_type_param(self, node):
        raise NotImplementedError('visit_type_param() must be implemented')

    def visit_var_decl(self, node):
        raise NotImplementedError('visit_var_decl() must be implemented')

    def visit_call_argument(self, node):
        raise NotImplementedError('visit_call_argument() must be implemented')

    def visit_field_decl(self, node):
        raise NotImplementedError('visit_field_decl() must be implemented')

    def visit_param_decl(self, node):
        raise NotImplementedError('visit_param_decl() must be implemented')

    def visit_func_decl(self, node):
        raise NotImplementedError('visit_func_decl() must be implemented')

    def visit_lambda(self, node):
        raise NotImplementedError('visit_lambda() must be implemented')

    def visit_func_ref(self, node):
        raise NotImplementedError('visit_func_ref() must be implemented')

    def visit_bottom_constant(self, node):
        raise NotImplementedError("visit_bottom_constant() must be implemented")

    def visit_integer_constant(self, node):
        raise NotImplementedError(
            'visit_integer_constant() must be implemented')

    def visit_real_constant(self, node):
        raise NotImplementedError('visit_real_constant() must be implemented')

    def visit_char_constant(self, node):
        raise NotImplementedError('visit_char_constant() must be implemented')

    def visit_string_constant(self, node):
        raise NotImplementedError(
            'visit_string_constant() must be implemented')

    def visit_array_expr(self, node):
        raise NotImplementedError(
            'visit_array_expr() must be implemented')

    def visit_boolean_constant(self, node):
        raise NotImplementedError(
            'visit_boolean_constant() must be implemented')

    def visit_variable(self, node):
        raise NotImplementedError('visit_variable() must be implemented')

    def visit_logical_expr(self, node):
        raise NotImplementedError('visit_logical_expr() must be implemented')

    def visit_equality_expr(self, node):
        raise NotImplementedError('visit_equality_expr() must be implemented')

    def visit_comparison_expr(self, node):
        raise NotImplementedError(
            'visit_comparison_expr() must be implemented')

    def visit_arith_expr(self, node):
        raise NotImplementedError('visit_arith_expr() must be implemented')

    def visit_conditional(self, node):
        raise NotImplementedError('visit_conditional() must be implemented')

    def visit_is(self, node):
        raise NotImplementedError('visit_is() must be implemented')

    def visit_new(self, node):
        raise NotImplementedError('visit_new() must be implemented')

    def visit_field_access(self, node):
        raise NotImplementedError('visit_field_access() must be implemented')

    def visit_func_call(self, node):
        raise NotImplementedError('visit_func_call() must be implemented')

    def visit_assign(self, node):
        raise NotImplementedError('visit_assign() must be implemented')


class DefaultVisitor(ASTVisitor):

    def result(self):
        raise NotImplementedError('result() must be implemented')

    def _visit_node(self, node):
        children = node.children()
        for c in children:
            c.accept(self)

    def visit_program(self, node):
        return self._visit_node(node)

    def visit_block(self, node):
        return self._visit_node(node)

    def visit_super_instantiation(self, node):
        return self._visit_node(node)

    def visit_class_decl(self, node):
        return self._visit_node(node)

    def visit_type_param(self, node):
        return self._visit_node(node)

    def visit_var_decl(self, node):
        return self._visit_node(node)

    def visit_call_argument(self, node):
        return self._visit_node(node)

    def visit_field_decl(self, node):
        return self._visit_node(node)

    def visit_param_decl(self, node):
        return self._visit_node(node)

    def visit_func_decl(self, node):
        return self._visit_node(node)

    def visit_lambda(self, node):
        return self._visit_node(node)

    def visit_func_ref(self, node):
        return self._visit_node(node)

    def visit_bottom_constant(self, node):
        return self._visit_node(node)

    def visit_integer_constant(self, node):
        return self._visit_node(node)

    def visit_real_constant(self, node):
        return self._visit_node(node)

    def visit_char_constant(self, node):
        return self._visit_node(node)

    def visit_string_constant(self, node):
        return self._visit_node(node)

    def visit_array_expr(self, node):
        return self._visit_node(node)

    def visit_boolean_constant(self, node):
        return self._visit_node(node)

    def visit_variable(self, node):
        return self._visit_node(node)

    def visit_logical_expr(self, node):
        return self._visit_node(node)

    def visit_equality_expr(self, node):
        return self._visit_node(node)

    def visit_comparison_expr(self, node):
        return self._visit_node(node)

    def visit_arith_expr(self, node):
        return self._visit_node(node)

    def visit_conditional(self, node):
        return self._visit_node(node)

    def visit_is(self, node):
        return self._visit_node(node)

    def visit_new(self, node):
        return self._visit_node(node)

    def visit_field_access(self, node):
        return self._visit_node(node)

    def visit_func_call(self, node):
        return self._visit_node(node)

    def visit_assign(self, node):
        return self._visit_node(node)


class DefaultVisitorUpdate(DefaultVisitor):

    def result(self):
        raise NotImplementedError('result() must be implemented')

    def _visit_node(self, node):
        children = node.children()
        new_children = []
        for c in children:
            if c is None:
                new_children.append(None)
                continue
            new_children.append(c.accept(self))
        node.update_children(new_children)
        return node


class FunctionDeclarationRemover(DefaultVisitorUpdate):
    def __init__(self):
        self.inside_inline_func = False
        self.removed_functions = []

    def result(self):
        return None

    def visit_func_decl(self, node):
        old_inside_inline_func = self.inside_inline_func
        if node.is_inline:
            self.inside_inline_func = True
            self.removed_functions.append(set())

        res = super().visit_func_decl(node)

        if node.is_inline:
            self.removed_functions.pop()
        self.inside_inline_func = old_inside_inline_func
        return res

    def visit_block(self, node):
        if self.inside_inline_func:

            current_removed = self.removed_functions[-1]
            for stmt in node.body:
                if isinstance(stmt, ast.FunctionDeclaration) and not stmt.is_inline:
                    current_removed.add(stmt.name)

            new_body = []
            for stmt in node.body:
                if isinstance(stmt, ast.FunctionDeclaration):
                    if not stmt.is_inline:
                        continue

                if isinstance(stmt, ast.FunctionCall) and stmt.func in current_removed:
                    continue
                
                visited_stmt = stmt.accept(self)
                if visited_stmt is not None:
                    new_body.append(visited_stmt)
            node.body = new_body
            return node
        return super().visit_block(node)

    def visit_func_call(self, node):
        if self.inside_inline_func:
            current_removed = self.removed_functions[-1]
            if node.func in current_removed:
                return None
        return super().visit_func_call(node)

    def visit_func_ref(self, node):
        if self.inside_inline_func:
            current_removed = self.removed_functions[-1]
            if node.func in current_removed:
                return None
        return super().visit_func_ref(node)
