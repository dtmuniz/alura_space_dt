from django import forms


class LoginForms(forms.Form):
    nome_login = forms.CharField(
        label='Nome de Login',
        required=True,
        max_length=100,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Ex.: João da Silva',
            }
        )
    )

    senha = forms.CharField(
        label='Senha',
        required=True,
        max_length=70,
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Digite a sua senha',
            }
        ),
    )

class CadastroForms(forms.Form):
    nome_cadastro = forms.CharField(
        label='Nome de Cadastro',
        required=True,
        max_length=100,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Ex.: João da Silva',
            }
        )
    )
    email_cadastro = forms.EmailField(
        label='Digite o seu email',
        required=True,
        max_length=100,
        widget=forms.EmailInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Ex.: joaosilva@gmail.com',
            }
        )
    )
    senha_cadastro = forms.CharField(
        label='Senha',
        required=True,
        max_length=70,
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Digite a sua senha',
            }
        ),
    )
    senha_confirma_cadastro = forms.CharField(
        label='Confirmar Senha',
        required=True,
        max_length=70,
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Digite a sua senha novamente',
            }
        ),
    )

    def clean_nome_cadastro(self):
        nome = self.cleaned_data.get("nome_cadastro")
        if nome:
            nome = nome.strip()
            if " " in nome:
                raise forms.ValidationError("Não é possível deixar espaços nesse campo")
            else:
                return nome
        

    def clean_senha_confirma_cadastro(self):
      senha_cadastro = self.cleaned_data.get("senha_cadastro")
      senha_confirma_cadastro = self.cleaned_data.get("senha_confirma_cadastro")

      if senha_cadastro and senha_confirma_cadastro:
            if senha_cadastro != senha_confirma_cadastro:
                raise forms.ValidationError("As senhas digitadas não são iguais!")
            else:
                return senha_confirma_cadastro