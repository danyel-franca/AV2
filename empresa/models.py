from django.db import models

class Empresa(models.Model):
    nomeEmpresa = models.CharField(max_length = 60)
    CNPJ = models.IntegerField(unique = True)
    endereco = models.CharField(max_length = 100)
    areaAtuacao = models.CharField(max_length = 100)

    def __str__(self):
        return self.nomeEmpresa

class Cargo(models.Model):
    empresa_FK = models.ForeignKey(Empresa, on_delete = models.CASCADE)
    cargoAtuante = models.CharField(max_length = 100)
    cargoNivel = models.CharField(max_length = 50)
    faixaSalarial = models.IntegerField()

    def __str__(self):
        return self.cargoAtuante

class Funcionario(models.Model):
    nomeFuncionario = models.CharField(max_length = 100)
    CPF = models.IntegerField(unique = True)
    empresa_FK = models.ForeignKey(Empresa, on_delete = models.CASCADE)
    cargo_FK = models.ForeignKey(Cargo, on_delete = models.CASCADE)
    dataAdmissao = models.DateTimeField(auto_now_add = True)
    emailCorporativo = models.EmailField(unique = True)

    def __str__(self):
        return self.nomeFuncionario