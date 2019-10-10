function validacao(){
			if (document.form.nome.value == ""){
				alert("Insira seu nome por favor.");
				document.form.nome.focus();
				return false;
			}
			if (document.form.sobrenome.value == ""){
				alert("Insira seu sobrenome por favor.");
				document.form.sobrenome.focus();
				return false;
			}
			if (document.form.idade.value < 18){
				alert("Somente para maiores de idade.");
				return false;
			}
			if (document.form.email.value == "" || document.form.email.value.indexOf('@')==-1 || document.form.email.value.indexOf('.')==-1){
				alert("Insira um email válido.");
				document.form.email.focus();
				return false;
			}
			if (document.form.senha.value.length < 6){
				alert("Preencha o campo senha.");
				document.form.senha.focus();
				return false;
			}
			if (document.form.rua.value == ""){
				alert("Insira seu endereço.");
				document.form.rua.focus();
				return false;
			}
			if (document.form.numero.value == ""){
				alert("Insira seu endereço.");
				document.form.numero.focus();
				return false;
			}
			if (document.form.bairro.value == ""){
				alert("Insira seu endereço.");
				document.form.bairro.focus();
				return false;
			}
			if (document.form.cep.value == ""){
				alert("Insira o CEP de sua cidade.");
				document.form.cep.focus();
				return false;
			}
			
			alert("Seu formulário foi enviado. OBRIGADO(A)!");
		}
		
		
function login(){
	if (document.form.email.value == "" || document.form.login.email.value.indexOf('@')==-1 || document.form.login.email.value.indexOf('.')==-1){
				alert("Insira um email válido.");
				document.form.email.focus();
				return false;
	}
	if (document.form.senha.value.length >= 6){
		alert("Preencha o campo senha.");
		document.form.senha.focus();
		return false;
	}
}