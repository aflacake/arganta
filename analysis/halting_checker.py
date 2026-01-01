# halting_checker.py

def verify_halting(ast):
    for stmt in ast:
        if stmt.type == "loop":
            if not stmt.has_proof:
                raise Exception("Loop tanpa bukti berhenti!")
    return True
