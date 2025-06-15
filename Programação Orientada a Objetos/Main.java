public class Main {
    public static void main(String[] args) {
        //copa
        Carta cAS, c2, c3, c4, c5, c6, c7, c8, c9, cREI, cCAV, cVEIA;
        //paus
        Carta pAS, p2, p3, p4, p5, p6, p7, p8, p9, pREI, pCAV, pVEIA;
        //espada
        Carta eAS, e2, e3, e4, e5, e6, e7, e8, e9, eREI, eCAV, eVEIA;
        //OURO
        Carta oAS, o2, o3, o4, o5, o6, o7, o8, o9, oREI, oCAV, oVEIA;
        try{


            //BARALHO
            Baralho b1 = new Baralho();

            //CARTAS DE PAUS
            b1.addCarta(pAS = new Carta("Ás","PAUS"));
            b1.addCarta(p2 = new Carta("2","PAUS"));
            b1.addCarta(p3 = new Carta("3","PAUS"));
            b1.addCarta(p4 = new Carta("4","PAUS"));
            b1.addCarta(p5 = new Carta("5","PAUS"));
            b1.addCarta(p6 = new Carta("6","PAUS"));
            b1.addCarta(p7 = new Carta("7","PAUS"));
            b1.addCarta(p8 = new Carta("8","PAUS"));
            b1.addCarta(p9 = new Carta("9","PAUS"));
            b1.addCarta(pREI = new Carta("REI","PAUS"));
            b1.addCarta(pCAV = new Carta("CAVALO","PAUS"));
            b1.addCarta(pVEIA = new Carta("VEIA","PAUS"));
            //CARTAS DE COPA
            b1.addCarta(cAS = new Carta("Ás","COPAS"));
            b1.addCarta(c2 = new Carta("2","COPAS"));
            b1.addCarta(c3 = new Carta("3","COPAS"));
            b1.addCarta(c4 = new Carta("4","COPAS"));
            b1.addCarta(c5 = new Carta("5","COPAS"));
            b1.addCarta(c6 = new Carta("6","COPAS"));
            b1.addCarta(c7 = new Carta("7","COPAS"));
            b1.addCarta(c8 = new Carta("8","COPAS"));
            b1.addCarta(c9 = new Carta("9","COPAS"));
            b1.addCarta(cREI = new Carta("REI","COPAS"));
            b1.addCarta(cCAV = new Carta("CAVALO","COPAS"));
            b1.addCarta(cVEIA = new Carta("VEIA","COPAS"));
            //CARTAS DE OURO
            b1.addCarta(oAS = new Carta("Ás","OURO"));
            b1.addCarta(o2 = new Carta("2","OURO"));
            b1.addCarta(o3 = new Carta("3","OURO"));
            b1.addCarta(o4 = new Carta("4","OURO"));
            b1.addCarta(o5 = new Carta("5","OURO"));
            b1.addCarta(o6 = new Carta("6","OURO"));
            b1.addCarta(o7 = new Carta("7","OURO"));
            b1.addCarta(o8 = new Carta("8","OURO"));
            b1.addCarta(o9 = new Carta("9","OURO"));
            b1.addCarta(oREI = new Carta("REI","OURO"));
            b1.addCarta(oCAV = new Carta("CAVALO","OURO"));
            b1.addCarta(oVEIA = new Carta("VEIA","OURO"));
            //CARTAS DE ESPADAS
            b1.addCarta(eAS = new Carta("Ás","ESPADA"));
            b1.addCarta(e2 = new Carta("2","ESPADA"));
            b1.addCarta(e3 = new Carta("3","ESPADA"));
            b1.addCarta(e4 = new Carta("4","ESPADA"));
            b1.addCarta(e5 = new Carta("5","ESPADA"));
            b1.addCarta(e6 = new Carta("6","ESPADA"));
            b1.addCarta(e7 = new Carta("7","ESPADA"));
            b1.addCarta(e8 = new Carta("8","ESPADA"));
            b1.addCarta(e9 = new Carta("9","ESPADA"));
            b1.addCarta(eREI = new Carta("REI","ESPADA"));
            b1.addCarta(eCAV = new Carta("CAVALO","ESPADA"));
            b1.addCarta(eVEIA = new Carta("VEIA","ESPADA"));


            //TESTE DE ERRO
            //Carta CORINGA = new Carta("CORINGA", "CORINGA");
            //b1.addCarta(CORINGA);

            System.out.println(b1.toString());

            System.out.println("A quantidade de cartas no baralho é: " + b1.quantasCartas());

            //b1.embaralhar();
            //System.out.println(b1.toString());

        }catch (Exception e){
            System.out.println(e.getMessage());
        }

    }
}