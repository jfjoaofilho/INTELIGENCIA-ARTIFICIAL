// Classe que representa uma regra na base de conhecimento
class Regra {
    private String condicao;
    private String conclusao;

    public Regra(String condicao, String conclusao) {
        this.condicao = condicao;
        this.conclusao = conclusao;
    }

    public boolean avaliar(String[] fatos) {
        // Avalia se a condição da regra é verdadeira com base nos fatos disponíveis
        // Neste exemplo, a condição é uma string simples que representa uma igualdade entre fatos
        return fatos[0].equals(condicao);
    }

    public String getConclusao() {
        return conclusao;
    }
}

// Classe que representa a base de conhecimento
class BaseDeConhecimento {
    private List<Regra> regras;

    public BaseDeConhecimento() {
        this.regras = new ArrayList<>();
    }

    public void adicionarRegra(Regra regra) {
        regras.add(regra);
    }

    public String inferir(String[] fatos) {
        // Realiza a inferência com base nos fatos disponíveis e retorna a conclusão obtida
        for (Regra regra : regras) {
            if (regra.avaliar(fatos)) {
                return regra.getConclusao();
            }
        }
        return "Conclusão não encontrada";
    }
}

// Classe principal que representa o sistema baseado em conhecimento
public class SistemaBaseadoEmConhecimento {
    public static void main(String[] args) {
        // Criação da base de conhecimento
        BaseDeConhecimento baseDeConhecimento = new BaseDeConhecimento();

        // Criação de regras
        Regra regra1 = new Regra("fato1", "conclusao1");
        Regra regra2 = new Regra("fato2", "conclusao2");

        // Adição das regras à base de conhecimento
        baseDeConhecimento.adicionarRegra(regra1);
        baseDeConhecimento.adicionarRegra(regra2);

        // Fatos de entrada para inferência
        String[] fatos = {"fato1"};

        // Inferência e obtenção da conclusão
        String conclusao = baseDeConhecimento.inferir(fatos);

        // Exibição da conclusão obtida
        System.out.println("Conclusão: " + conclusao);
    }
}
