<div align="center">
  <h1>Deteksi Sampah di Permukaan Air (Floating Marine Litter) menggunakan YOLO</h1>
  <h3>RSBP (B) - Kelompok 6</h3>

  | Name             | NRP              |
|------------------|-------------|
| Rumaisha Afrina        | 5025221146          |
| Helsa Sriprameswari Putri      | 5025221154         |
| Aurelia Natasya Putri       | 5025221237          |

</div>


# Introduction 
Masalah sampah di lautan telah menjadi tantangan global yang semakin mendesak seiring meningkatnya aktivitas manusia dan pertumbuhan populasi. Sampah laut, terutama sampah yang mengapung di permukaan air, tidak hanya mencemari lingkungan tetapi juga mengancam ekosistem laut, kehidupan laut, dan kesehatan manusia. Data dari berbagai penelitian menunjukkan bahwa jumlah sampah di lautan terus meningkat, dengan plastik menjadi salah satu komponen utama. Oleh karena itu, deteksi dan pemantauan sampah di permukaan air menjadi krusial untuk upaya pembersihan dan pengelolaan sampah.

Teknologi pengenalan objek berbasis kecerdasan buatan, khususnya model You Only Look Once (YOLO), menawarkan solusi yang efisien untuk mendeteksi dan mengklasifikasikan objek dalam waktu nyata. Dengan kemampuan untuk memproses gambar secara cepat dan akurat, YOLO dapat digunakan untuk mengidentifikasi berbagai jenis sampah yang mengapung di permukaan laut. Implementasi YOLO dalam deteksi sampah di permukaan air tidak hanya memungkinkan pemantauan yang lebih baik tetapi juga memberikan data yang diperlukan untuk merancang strategi pengelolaan yang efektif.

Penelitian ini bertujuan untuk mengeksplorasi penerapan algoritma YOLO dalam mendeteksi sampah laut yang mengapung, serta untuk menganalisis efektivitas metode ini dalam meningkatkan upaya pembersihan lingkungan laut. Dengan pendekatan yang inovatif ini, diharapkan dapat memberikan kontribusi positif dalam melindungi ekosistem laut dan menciptakan kesadaran akan pentingnya menjaga kebersihan lautan.


# Method
![image](https://github.com/user-attachments/assets/9f237722-abd0-4ab4-a801-8c8d9b627cae)

## 1. Creating Datasets
Proses ini dimulai dengan pemanfaatan kamera pengawas, seperti kamera drone atau kamera yang dipasang di kapal, untuk merekam gambar atau video dari permukaan air. Penting untuk memperhatikan kondisi pencatatan, seperti waktu, cuaca, dan variasi lingkungan, guna memastikan kualitas gambar yang diambil. Jika dataset yang relevan sudah tersedia, tim dapat memanfaatkannya; jika tidak, mereka perlu membangun dataset baru dengan merekam gambar secara manual dan memberi label pada setiap gambar. Seluruh pengambilan data harus didokumentasikan dengan baik, mencakup informasi seperti lokasi, waktu, dan kondisi lingkungan, untuk mendukung analisis lebih lanjut. 

## 2. Prepocessing Data
Sebelum model YOLO diterapkan, data yang dikumpulkan perlu diproses terlebih dahulu untuk memastikan kualitasnya sesuai dengan kebutuhan model, atau sebuah proses yang disebut dengan preprocessing.

![preprocessing](https://github.com/rumaishafrn/RSBP_PROJECT/blob/main/img/preprocessing.png)

Preprocessing seperti labelling, split data, auto-orient, resize, dan augmentation yang dimana berguna untuk pengembangan dataset akhir. Dengan mengubah data mentah menjadi data yang siap untuk dilatih. Dalam konteks ini, preprocessing data menjadi langkah yang penting, yang melibatkan serangkaian teknik dan metode untuk membersihkan, mengubah, dan memformat data agar dapat diproses oleh algoritma Machine Learning atau analisis data.

## 3. Implementasi algoritma You Only Look Once (YOLO)

Algoritma You Only Look Once (YOLO) dikenal sebagai metode yang cepat dan akurat dalam deteksi objek, membuatnya sangat sesuai untuk aplikasi yang memerlukan analisis real-time (Amwin, 2021). YOLO melakukan analisis gambar secara keseluruhan dalam satu tahap. Pendekatan ini memungkinkan deteksi objek dalam waktu yang singkat, menjadikannya pilihan ideal untuk proyek deteksi sampah di permukaan air. Sebagai algoritma yang relatif baru, YOLO menawarkan berbagai keunggulan dibandingkan metode sebelumnya, termasuk kemampuan untuk mendeteksi berbagai jenis objek secara bersamaan.

Proses implementasi YOLO dilakukan menggunakan Google Collaboratory, yang menyediakan lingkungan yang mudah digunakan untuk pengembangan model machine learning. Langkah pertama adalah penyiapan model YOLO versi 5, yang dikenal dengan efisiensinya yang tinggi. Setelah itu, dataset diambil dari Roboflow atau Kaggle, platform yang menawarkan berbagai dataset terstruktur untuk pelatihan model. Dataset yang tepat dan berkualitas tinggi sangat penting dalam proses ini, karena dapat mempengaruhi kinerja model dalam mendeteksi sampah dengan akurat. Pelatihan model melibatkan teknik augmentasi data, yang meningkatkan variasi dalam dataset untuk memastikan bahwa model dapat mengenali objek dalam berbagai kondisi pencahayaan dan sudut pandang.


# YOLO v5 Installation


# Datasets
![image](https://github.com/user-attachments/assets/43201a33-58ce-4aae-8e54-44986d6c0979)

# Output


