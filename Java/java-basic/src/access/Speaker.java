package access;

public class Speaker {
    private int volume;

    Speaker(int volume) {
        this.volume = volume;
    }
    void volumeUp () {
        if (volume >= 100) {
            System.out.println("최대 음량입니다.");
        } else {
            volume += 10;
            System.out.println("음량 10 증가");
        }
    }
    void volumeDown() {
        if (volume <= 0) {
            System.out.println("최소 음량입니다.");
        } else {
            volume -= 10;
            System.out.println("음량 10 감소");
        }
    }
    void showVolume() {
        System.out.println("현재 음량 : " + volume);
    }
}
