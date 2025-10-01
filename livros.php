<?php

$livros = array(
    array("nome" => "Dom Casmurro", "genero" => "Romance", "paginas" => 256),
    array("nome" => "O Senhor dos Anéis", "genero" => "Fantasia", "paginas" => 1200),
    array("nome" => "1984", "genero" => "Distopia", "paginas" => 328),
    array("nome" => "A Revolução dos Bichos", "genero" => "Satírico", "paginas" => 152)
);

echo "<h2>Lista de Livros</h2>";
echo "<table border='1' cellpadding='5' cellspacing='0'>";
echo "<tr><th>Nome</th><th>Gênero</th><th>Páginas</th></tr>";

foreach($livros as $livro){
    echo "<tr>";
    echo "<td>".$livro['nome']."</td>";
    echo "<td>".$livro['genero']."</td>";
    echo "<td>".$livro['paginas']."</td>";
    echo "</tr>";
}

echo "</table>";

?>