package com.aryankumar.pulsetrack;

import android.app.Activity;
import android.os.Bundle;
import android.webkit.WebSettings;
import android.webkit.WebView;
import android.webkit.WebViewClient;
import android.widget.FrameLayout;

public class MainActivity extends Activity {
    private WebView webView;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);

        FrameLayout layout = new FrameLayout(this);
        webView = new WebView(this);
        layout.addView(webView);
        setContentView(layout);

        WebSettings settings = webView.getSettings();
        settings.setJavaScriptEnabled(true);
        settings.setDomStorageEnabled(true);
        settings.setLoadWithOverviewMode(true);
        settings.setUseWideViewPort(true);

        webView.setWebViewClient(new WebViewClient());
        
        // PulseTrack Embedded Native Experience
        String htmlContent = "<!DOCTYPE html><html><head><meta name='viewport' content='width=device-width, initial-scale=1.0'>" +
            "<style>body{background:#0F172A;color:#F8FAFC;font-family:sans-serif;margin:0;padding:24px;text-align:center;}" +
            ".card{background:#1E293B;border-radius:16px;padding:24px;margin-top:20px;border:1px solid #334155;}" +
            ".btn{background:#6366F1;color:white;border:none;padding:12px 24px;border-radius:12px;font-weight:bold;margin-top:16px;width:100%;}" +
            "</style></head><body>" +
            "<h2>PulseTrack Mobile</h2>" +
            "<p style='color:#94A3B8;font-size:14px;'>Modern Offline-First Productivity Suite</p>" +
            "<div class='card'>" +
            "<h3>Today's Focus: 100% Target</h3>" +
            "<p style='color:#38BDF8;'>Autonomous Model Factory Active</p>" +
            "<button class='btn' onclick='alert(\"Feature logged!\")'>Check In Progress</button>" +
            "</div></body></html>";

        webView.loadDataWithBaseURL(null, htmlContent, "text/html", "utf-8", null);
    }

    @Override
    public void onBackPressed() {
        if (webView.canGoBack()) {
            webView.goBack();
        } else {
            super.onBackPressed();
        }
    }
}
