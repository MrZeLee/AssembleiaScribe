# AssembleiaScribe

AssembleiaScribe is an early-stage project designed to automate the processing
of ARTV videos from Portuguese Assembleia da República meetings. The pipeline
extracts audio, transcribes speech using OpenAI’s Whisper-1, segments speakers
with pyannote.ai, and identifies speakers with contextual assistance from
ChatGPT. The end result is a speaker-attributed transcript and meeting summary
for web publication.

## Project Vision

- **Automated Processing:**  
  Detect new ARTV meeting videos automatically and trigger the processing
  pipeline.
- **Accurate Transcription:**  
  Use Whisper-1 to generate high-quality, timestamped transcripts.
- **Speaker Diarization & Identification:**  
  Segment audio into speaker turns using pyannote.ai and identify speakers with
  ChatGPT when voiceprints are not initially recognized.
- **Content Publication:**  
  Produce and publish meeting summaries and full transcripts (e.g., on GitHub
  Pages).

## Planned Architecture

1. **Video Detection:**  
   Monitor ARTV for new meeting videos via scheduled checks or webhooks.
2. **Audio Extraction:**  
   Use tools like ffmpeg to extract and preprocess audio from video files.
3. **Transcription:**  
   Process audio with Whisper-1 to produce timestamped transcripts.
4. **Speaker Diarization:**  
   Apply pyannote.ai to segment the transcript by speaker.
5. **Speaker Identification:**  
   Utilize ChatGPT to analyze transcript context for unknown speakers and update
   the voiceprint database.
6. **Web Publishing:**  
   Generate and publish transcripts and meeting summaries for easy access and
   review.

## Development & DevOps Strategy

- **Modular Pipeline:**  
  Develop each component (video detection, transcription, diarization,
  identification, publishing) as an independent module for easier testing,
  maintenance, and scalability.
- **Repository Structure:**  
  Start with a monorepo featuring clearly separated directories (e.g.,
  `/video_detector`, `/transcription`, `/diarization`, `/web_publish`). As the
  project evolves, consider splitting modules into separate repositories for
  enhanced isolation and independent deployment.
- **CI/CD & Containerization:**  
  Set up continuous integration (e.g., GitHub Actions) and containerize
  components using Docker to ensure consistent environments from development to
  production.
- **Monitoring & Logging:**  
  Integrate robust logging and monitoring to track pipeline performance and
  simplify debugging.

## Contributing

Feedback and contributions are welcome. Please use the issue tracker or submit
pull requests with clear descriptions of any changes. Additional documentation
and setup instructions will be added as the project matures.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file
for details.
