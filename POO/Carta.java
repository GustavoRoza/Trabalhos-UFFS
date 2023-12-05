public class Carta extends Baralho{
    private String numero;
    private String naipe;

    public Carta(String numero, String naipe) throws Exception{
        if (naipe != "PAUS" && naipe != "OURO" && naipe != "ESPADA" && naipe != "COPAS"){
            throw new Exception("NAIPE INVÁLIDO");
        }else{
            this.numero =  numero;
            this.naipe = naipe;
        }
    }
    public String getNumero(){
        return this.numero;
    }

    public String getNaipe(){
        return this.naipe;
    }

    @Override
    public String toString() {
        return "\nCarta: " +numero + " de " + naipe;
    }
}
