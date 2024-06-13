package com.example.demoshop;

import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.ResponseBody;

import java.time.ZonedDateTime;

@Controller
public class BasicController {
    @GetMapping("/")
    String hello() {
        return "index.html";
    }
    @GetMapping("/about")
    @ResponseBody
    String gg() {
        return "안녕?";
    }
    @GetMapping("/mypage")
    @ResponseBody
    String ggg() {
        return "my";
    }
    @GetMapping("/date")
    @ResponseBody
    String date() {
        return ZonedDateTime.now().toString();
    }
}
