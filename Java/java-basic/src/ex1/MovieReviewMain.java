package ex1;

public class MovieReviewMain {
    public static void main(String[] args) {
        MovieReview review1 = new MovieReview();
        review1.title = "인셉션";
        review1.review = "재밌다~";

        MovieReview review2 = new MovieReview();
        review2.title = "어바웃타임";
        review2.review = "아주 재밌다~";

        MovieReview[] reviews = new MovieReview[]{review1,review2};

        for (int i = 0; i < reviews.length; i++) {
            MovieReview rv = reviews[i];
            System.out.println("영화 제목 : " + rv.title + ", 리뷰 : " + rv.review);
        }

    }
}
