from core.infrastructure.repository_implementation.responsavelCrasSidsRepositoryImpl import ResponsavelCrasSidsRepositoryImpl


r = ResponsavelCrasSidsRepositoryImpl()

result = r.recuperar_responsavel_cras('igor.costa')

print(result)
print(result.all())
