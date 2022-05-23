package com.example.corelibrarymanager;
import androidx.appcompat.app.ActionBar;
import androidx.appcompat.app.AppCompatActivity;
import androidx.recyclerview.widget.RecyclerView;

import android.content.Context;
import android.os.Bundle;
import android.util.Log;
import android.view.KeyEvent;
import android.widget.EditText;
import android.view.inputmethod.EditorInfo;
import android.widget.TextView;
import com.google.android.material.card.MaterialCardView;

import org.json.JSONArray;
import org.json.JSONObject;

import java.io.IOException;
import java.io.InputStream;
import java.util.ArrayList;
import java.util.Vector;


public class FullscreenActivity extends AppCompatActivity {
    MaterialCardView itemCard;
    ArrayList<String> items; //Used to store the inputted items for the list
    ArrayList<String> times; //When each item was placed in the list
    String[] strings;
    EditText textInput;
    RecyclerView recyclerView;
    private RecyclerView.Adapter adapter;
    private RecyclerView.LayoutManager layoutManager;


    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        ActionBar actionBar = getSupportActionBar();
        actionBar.hide();
        setContentView(R.layout.activity_fullscreen);


//        itemCard = findViewById(R.id.itemCard);
//        recyclerView = findViewById(R.id.recyclerView);

        //Setting up text input
        textInput = findViewById(R.id.textInput);
        TextView.OnEditorActionListener exampleListener = new TextView.OnEditorActionListener() {
            public boolean onEditorAction(TextView exampleView, int actionId, KeyEvent event) {
                if((event != null && (event.getKeyCode()==KeyEvent.KEYCODE_ENTER && event.getAction() == KeyEvent.ACTION_DOWN)) || (actionId == EditorInfo.IME_ACTION_SEND)) {
                    if(!textInput.getText().toString().matches("")) {
//                        addItem(textInput.getText().toString());
                        recyclerView.scrollToPosition(0);
                    }
                }
                return true;
            }
        };
        textInput.setOnEditorActionListener(exampleListener);

        Vector<Book> bookList = getJSON();



    }

    public Vector<Book> getJSON() {
        String jsonString;
        Vector<Book> books = new Vector<Book>();

        try {
            InputStream inputStream = getAssets().open("coretexBooks.json");
            int size = inputStream.available();
            byte[] buffer = new byte[size];
            inputStream.read(buffer);
            inputStream.close();

            jsonString = new String(buffer, "UTF-8");
//            JSONObject jsonobject = new JSONObject(jsonString);
            JSONArray jsonArray = new JSONArray(jsonString);
            System.out.println("HI THERE LOL CAN YOU SEE MEEEEEEEEEE");

            for(int i = 0; i < jsonArray.length();i++){
                JSONObject obj = jsonArray.getJSONObject(i);
                Book book = new Book();
                book.title = obj.getString("Title");
                if(obj.has("Author")){
                    book.author = obj.getString("Author");
                }
                if(obj.has("ISBN")){
                    book.author = obj.getString("ISBN");
                }
                if(obj.has("Genre")){
                    book.author = obj.getString("Genre");
                }
                if(obj.has("Rented")){
                    book.author = obj.getString("Rented");
                }

                books.add(book);
            }


        } catch (Exception e) {
            e.printStackTrace();
        }

        return books;
    }

    class Book {
        public String title;
        public String author;
        public String isbn;
        public String genre;
        public String rented;
    }



}

