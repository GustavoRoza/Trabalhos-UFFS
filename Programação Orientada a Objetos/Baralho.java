import java.util.ArrayList;
import java.util.Collections;


public class Baralho {
    private ArrayList<Carta> cartas;

    public Baralho() {
        cartas = new ArrayList<Carta>();

    }

    public void addCarta(Carta carta) throws Exception{
        if (this.cartas.size() < 48)
            cartas.add(carta);
        else
            throw new Exception("Baralho cheio!");
    }

    public int quantasCartas() {

        int count = 0;
        for (int i = 0; i < this.cartas.size(); i++) {

            if (cartas.get(i) != null) {
                count++;
            }

        }
        return count;
    }
    public void embaralhar(){
        Collections.shuffle(this.cartas);
    }

    @Override
    public String toString() {
        return "Baralho: \n" + cartas + "\n";
    }


}