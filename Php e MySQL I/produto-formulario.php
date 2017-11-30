<?php include("cabecalho.php")?>
	<h1>Formulário de Produto</h1>
	<form action="adiciona-produto.php">
		Nome:
		<input type="text" name="nome">
		Preco:
		<input type="number" name="preco">

		<input type="submit" name="Cadastrar">
	</form>
<?php include("rodape.php")?>