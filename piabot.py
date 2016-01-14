#!/usr/bin/python
import telegram
import logging
import random

class PIABot:

	def __init__(self, total = False):
		self.bot_token = 'YOUR-BOT-TOKEN-HERE'
		self.channel = '@perubatanislamdanalternatif'
		self.total = total
		self.amalan_count = 0
		self.petua_count = 0
		self.Updater = telegram.Updater
		# Enable logging
		logging.basicConfig(
		        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
		        level=logging.INFO)

		self.logger = logging.getLogger(__name__)


	def count_amalan(self):
		if self.amalan_count > self.total:
			self.amalan_count = 1
		else:
			self.amalan_count = self.amalan_count + 1
		return self.amalan_count

	def count_petua(self):
		if self.petua_count > self.total:
			self.petua_count = 1
		else:
			self.petua_count = self.petua_count + 1
		return self.petua_count

	def updateAmalan(bot, self):

		amalan = [
			"Assalamualaikum. Ini ialah bot perubatan islam dan alternatif. Bot ini akan update mesej di channel Perubatan Islam/Alternatif.",
			"Amalkan ma'thurat sughro setiap pagi dan petang sebagai rutin harian.",
			"[Penawar sihir pengasih/pelaris] : Amalkan surah Al-Kauthar dengan niat untuk menawarkan/membatalkan sihir.",
			"[Penawar sihir pemisah/pelalau] : Amalkan ayat 256 dalam surah Al-Baqarah dengan niat untuk memulih/membatalkan sihir.",
			"[Penawar sihir santau] : Amalkan surah Al-Ikhlas dengan niat memulih/membatalkan sihir.",
			"[Pembatal saka / sihir] : Amalkan selawat penggerak (ayat kelima dalam bismillah 5) dengan niat memulih/membatalkan sihir.",
			"Doa atau ayat Al-Quran yang dibaca boleh diisi pada air atau apa-apa sahaja medium.",
			"Terima kasih kerana menggunakan bot perubatan islam dan alternatif",
			"Ingin mempunyai bot auto update channel seperti ini? emailkan idea anda ke mweldan@gmail.com",
			"Faedah beramal dengan ayat Al-Quran ialah kalau doa tak makbul kita dapat pahala. Faham dan amal.",
			"Ingin mengiklankan produk terapi anda di sini? Hubungi melalui mweldan@gmail.com . Kadar caj mengikut budi bicara.",
		]

		total = PIABot(len(amalan))
		message = amalan[total.amalan_count()]  
		bot.sendMessage(chat_id = self.channel, text = message)

	def updatePetua(bot, self):

		petua = [
			"[Petua] : Membangkitkan rasa ingin bertaubat: Amalkan surah Al-asr ketika solat.",
			"[Petua] : Penyakit Batu Karang : Makan betik, sebelum makan baca : Taawuz, Bismillah, dan Selawat 3 kali.",
			"[Petua] : Penyakit Buasir : Makan daging, sedekahkan surah Al-Fatihah pada muslimin dan muslimat, ada dan tiada.",
			"[Petua] : Penyakit Sembelit : Minum air masak, sedekahkan surah Al-Fatihah pada muslimin dan muslimat, ada dan tiada.",
			"[Petua] : Penyakit Angin Pasang : Sentuh, usap atau genggam tempat yang terkena angin pasang, ucapkan Subhanallah, Alhamdulillah, Allahuakbar.",
			"[Petua] : Penyakit Gout : Sapu minyak sapuan atau apa-apa sahaja minyak yang ada pada tempat terkena gout, ucapkan Nikmat Tuhan Yang Manakah Kamu Dustakan? (Di ambil dari surah Ar-Rahman)",
			"[Petua] : Penyakit Kencing Manis : Minum atau makan benda-benda masam, sebelum makan baca Taawuz, Bismillah, Selawat 3 kali dan sedekahkan surah Al-Fatihah pada muslimin-muslimat ada dan tiada.",
			"[Petua] : Penyakit Senggugut : Minum air masak, sebelum minum baca doa lupa baca doa makan.",
			"[Petua] : Penyakit Gila,Sawan,Jiwa Kacau dan seumpamanya : Zikir Allah 33 kali dengan niat mahu bahagia menikmati dugaan hidup seperti insan lain.",
			"[Petua] : Mudah menghafaz : Baca Allahumma solli 3ala sayyidina muhammad kamala niha yatalikamalihi wa3adada kamalih sebanyak 33 kali sebelum menghafaz apa-apa.",
			"[Petua] : Penyakit Beguk,Bisul dan seumpamanya : Baca selawat 3 kali dan sapu minyak sapuan apa-apa sahaja.",
			"[Petua] : Penyakit Kurap,Panau dan seumpamanya : Baca Subhanallah, Alhamdulillah, Allahuakbar dan usap tempat terkena penyakit.",
			"[Petua] : Penyakit Jantung, Kanser dan seumpamanya : Baca surah Al-Kauthar 3 kali dan tepuk tempat terkena penyakit 3 kali.",
			"[Petua] : Penyakit Angin Ahmar / Stroke : Baca Taawuz, Bismillah, Selawat 3 kali, Al-Fatihah sekali, usap pada tempat yang kaku.",
			"[Petua] : Penyakit Mandul / Tidak subur : Baca Taawuz, Bismillah, kemudian Subhanallah, Alhamdulillah, Allahuakbar 3 kali dan makan tembikai sepotong seorang (sekelamin).",

		]

		total = PIABot(len(petua))
		current = total.count_petua()
		message = petua[int(current)]  
		bot.sendMessage(chat_id = self.channel, text = message)

	def error(bot, update, error, self):
	    self.logger.warn('Update "%s" caused error "%s"' % (update, error))

	def main(self):
		updater = self.Updater(token = self.bot_token)
		dispatcher = updater.dispatcher

		job = updater.job_queue
		job.put(PIABot().updateAmalan, 300)
		job.put(PIABot().updatePetua, 60)

		updater.start_polling()

		updater.idle()

		updater.addErrorHandler(error)

if __name__ == "__main__":
	PIABot().main()