using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;
using System.IO.Ports;

namespace carControl
{
    public partial class Form1 : Form
    {
        String[] ports;
        SerialPort port;

        public Form1()
        {
            InitializeComponent();

            getAvailableComPorts();

            foreach (string port in ports)
            {
                comboBox1.Items.Add(port);
                Console.WriteLine(port);
                if (ports[0] != null)
                {
                    comboBox1.SelectedItem = ports[0];
                }
            }

            
        }

        private void forwardButton_MouseHover(object sender, EventArgs e)
        {
            try { port.Write("#FWRD\n"); }
            catch (Exception) { }

            forwardButton.BackColor = Color.FromArgb(64, 64, 64);
        }

        private void forwardButton_MouseLeave(object sender, EventArgs e)
        {
            try { port.Write("#FWR0\n"); }
            catch (Exception) {}

            forwardButton.BackColor = Color.FromArgb(224, 224, 224);
        }

        private void backButton_MouseHover(object sender, EventArgs e)
        {
            try { port.Write("#BACK\n"); }
            catch (Exception) {}

            backButton.BackColor = Color.FromArgb(64, 64, 64);
        }

        private void backButton_MouseLeave(object sender, EventArgs e)
        {
            try { port.Write("#BAC0\n"); }
            catch (Exception) {}

            backButton.BackColor = Color.FromArgb(224, 224, 224);
        }

        private void rightButton_MouseHover(object sender, EventArgs e)
        {
            try { port.Write("#RGHT\n"); }
            catch (Exception) {}

            rightButton.BackColor = Color.FromArgb(64, 64, 64);
        }

        private void rightButton_MouseLeave(object sender, EventArgs e)
        {
            try { port.Write("#RGH0\n"); }
            catch (Exception) {}

            rightButton.BackColor = Color.FromArgb(224, 224, 224);
        }

        private void leftButton_MouseHover(object sender, EventArgs e)
        {
            try { port.Write("#LEFT\n"); }
            catch (Exception) {}

            leftButton.BackColor = Color.FromArgb(64, 64, 64);
        }

        private void leftButton_MouseLeave(object sender, EventArgs e)
        {
            try { port.Write("#LEF0\n"); }
            catch (Exception) {}

            leftButton.BackColor = Color.FromArgb(224, 224, 224);
        }

        private void connectButton_Click(object sender, EventArgs e)
        {
            try
            {
                string selectedPort = comboBox1.GetItemText(comboBox1.SelectedItem);
                port = new SerialPort(selectedPort, 9600, Parity.None, 8, StopBits.One);
                port.Open();

                comboBox1.Enabled = false;
                connectButton.Enabled = false;
            }
            catch (Exception) { MessageBox.Show("port nem található"); }
        }

        void getAvailableComPorts()
        {
            ports = SerialPort.GetPortNames();
        }

        private void Form1_KeyDown(object sender, KeyEventArgs e)
        {

            
            switch (e.KeyCode)
            {
                case Keys.S:
                    try { port.Write("#BACK\n"); }
                    catch (Exception) { };
                    backButton.BackColor = Color.FromArgb(64, 64, 64);
                    
                    break;

                case Keys.W:
                    try { port.Write("#FWRD\n"); }
                    catch (Exception) { };
                    forwardButton.BackColor = Color.FromArgb(64, 64, 64);
                    break;

                case Keys.A:
                    try { port.Write("#LEFT\n"); }
                    catch (Exception) { };
                    leftButton.BackColor = Color.FromArgb(64, 64, 64);
                    break;

                case Keys.D:
                    try { port.Write("#RGHT\n"); }
                    catch (Exception) { };
                    rightButton.BackColor = Color.FromArgb(64, 64, 64);
                    break;
            }
            
        }

        private void Form1_KeyUp(object sender, KeyEventArgs e)
        {
            
            switch (e.KeyCode)
            {
                case Keys.S:
                    try { port.Write("#BAC0\n"); }
                    catch (Exception) { };
                    backButton.BackColor = Color.FromArgb(224, 224, 224);
                    break;

                case Keys.W:
                    try { port.Write("#FWR0\n"); }
                    catch (Exception) { };
                    forwardButton.BackColor = Color.FromArgb(224, 224, 224);
                    break;

                case Keys.A:
                    try { port.Write("#LEF0\n"); }
                    catch (Exception) { };
                    leftButton.BackColor = Color.FromArgb(224, 224, 224);
                    break;

                case Keys.D:
                    try { port.Write("#RGH0\n"); }
                    catch (Exception) { };
                    rightButton.BackColor = Color.FromArgb(224, 224, 224);
                    break;
            }
            
        }

        private void button1_Click(object sender, EventArgs e)
        {
            try {
                port.Write("#INTF" + latency.Text + "\n");
                port.Write("#INTB" + latency2.Text + "\n");
            }
            //MessageBox.Show("#" + latency.Text + "\n");
            //try { port.Write("#RGHT\n"); }
            catch (Exception) { };
        }
    }
}
