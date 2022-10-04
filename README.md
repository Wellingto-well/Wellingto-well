    String titulo;
    String autor;
    int paginas;
    double preco;
    
    CadastroLivro(String tituloArg, String autorArg){
        titulo = tituloArg;
        autor = autorArg;
    }
    String GetAutor(){
        return autor;
    }
    String GetTitulo(){
        return titulo;
    }
    void SetAutor(String tituloArg){
        titulo = tituloArg;
    }
    void SetTitulo(String autorArg){
        autor = autorArg;
    }
    void PrintNatela(){
        System.out.println("Autor "+ autor);
        System.out.println("Titulo "+ titulo);
        System.out.println("Paginas "+ paginas);
        System.out.println("Preço "+ preco);
    }
    
    |||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
    
    
    CadastroLivro livro1 = new CadastroLivro("python Data Scienty", "Wellington");
       System.out.println(livro1.GetTitulo() + ", " + livro1.GetAutor() ); 
