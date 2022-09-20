new Vue({
  el: '#app',// index.htmlでid="app"となっている要素（エレメント）を指定
  data: {
      input: ''// index.htmlでv-model="input"が付与されている要素と双方向データバインディングされている。
  },
  computed: {
      convertMarkdown: function() {
          // index.htmlでv-html="convertMarkdown"が付与されている要素（エレメント）とバイディングされている。
          // 入力されたデータをHTMLに変換して表示させる。
          return marked(this.input);
      }
  }
})