<?php 
	include("cabecalho.php");
	include("conecta.php");
	$nome = $_GET["nome"];
	$preco = $_GET["preco"];
	$descricao = $_GET['descricao'];
	

	function insereProduto($conexao, $nome, $preco, $descricao) {
	    $query = "insert into produtos (nome, preco, descricao) values ('{$nome}', {$preco}, '{$descricao}')";
	    $resultadoDaInsercao = mysqli_query($conexao, $query);
	    return $resultadoDaInsercao;
	}


	if(insereProduto($conexao, $nome, $preco, $descricao)) {
?>
		<h2 class="alert-success">Produto <?= $nome; ?>, <?= $preco; ?> adicionado com sucesso!</h2>
	<?php
		} else {
	    $msg = mysqli_error($conexao);
	?>
		<h2 class="alert-danger">O produto <? = $nome; ?> não foi adicionado: <?= $msg ?></h2>
	<?php
		}
	?>
<?php include("rodape.php")?>