namespace carControl
{
    partial class Form1
    {
        /// <summary>
        /// Required designer variable.
        /// </summary>
        private System.ComponentModel.IContainer components = null;

        /// <summary>
        /// Clean up any resources being used.
        /// </summary>
        /// <param name="disposing">true if managed resources should be disposed; otherwise, false.</param>
        protected override void Dispose(bool disposing)
        {
            if (disposing && (components != null))
            {
                components.Dispose();
            }
            base.Dispose(disposing);
        }

        #region Windows Form Designer generated code

        /// <summary>
        /// Required method for Designer support - do not modify
        /// the contents of this method with the code editor.
        /// </summary>
        private void InitializeComponent()
        {
            this.comboBox1 = new System.Windows.Forms.ComboBox();
            this.connectButton = new System.Windows.Forms.Button();
            this.forwardButton = new System.Windows.Forms.Button();
            this.leftButton = new System.Windows.Forms.Button();
            this.backButton = new System.Windows.Forms.Button();
            this.rightButton = new System.Windows.Forms.Button();
            this.button1 = new System.Windows.Forms.Button();
            this.latency = new System.Windows.Forms.TextBox();
            this.latency2 = new System.Windows.Forms.TextBox();
            this.SuspendLayout();
            // 
            // comboBox1
            // 
            this.comboBox1.FormattingEnabled = true;
            this.comboBox1.Location = new System.Drawing.Point(154, 170);
            this.comboBox1.Name = "comboBox1";
            this.comboBox1.Size = new System.Drawing.Size(111, 24);
            this.comboBox1.TabIndex = 0;
            // 
            // connectButton
            // 
            this.connectButton.Location = new System.Drawing.Point(271, 170);
            this.connectButton.Name = "connectButton";
            this.connectButton.Size = new System.Drawing.Size(74, 23);
            this.connectButton.TabIndex = 1;
            this.connectButton.Text = "connect";
            this.connectButton.UseVisualStyleBackColor = true;
            this.connectButton.Click += new System.EventHandler(this.connectButton_Click);
            // 
            // forwardButton
            // 
            this.forwardButton.BackColor = System.Drawing.Color.FromArgb(((int)(((byte)(224)))), ((int)(((byte)(224)))), ((int)(((byte)(224)))));
            this.forwardButton.Location = new System.Drawing.Point(145, 12);
            this.forwardButton.Name = "forwardButton";
            this.forwardButton.Size = new System.Drawing.Size(62, 53);
            this.forwardButton.TabIndex = 2;
            this.forwardButton.Text = "FWRD";
            this.forwardButton.UseVisualStyleBackColor = false;
            this.forwardButton.MouseEnter += new System.EventHandler(this.forwardButton_MouseHover);
            this.forwardButton.MouseLeave += new System.EventHandler(this.forwardButton_MouseLeave);
            // 
            // leftButton
            // 
            this.leftButton.Location = new System.Drawing.Point(73, 71);
            this.leftButton.Name = "leftButton";
            this.leftButton.Size = new System.Drawing.Size(62, 53);
            this.leftButton.TabIndex = 3;
            this.leftButton.Text = "LEFT";
            this.leftButton.UseVisualStyleBackColor = true;
            this.leftButton.MouseEnter += new System.EventHandler(this.leftButton_MouseHover);
            this.leftButton.MouseLeave += new System.EventHandler(this.leftButton_MouseLeave);
            // 
            // backButton
            // 
            this.backButton.Location = new System.Drawing.Point(145, 71);
            this.backButton.Name = "backButton";
            this.backButton.Size = new System.Drawing.Size(62, 53);
            this.backButton.TabIndex = 4;
            this.backButton.Text = "BACK";
            this.backButton.UseVisualStyleBackColor = true;
            this.backButton.MouseEnter += new System.EventHandler(this.backButton_MouseHover);
            this.backButton.MouseLeave += new System.EventHandler(this.backButton_MouseLeave);
            // 
            // rightButton
            // 
            this.rightButton.Location = new System.Drawing.Point(213, 71);
            this.rightButton.Name = "rightButton";
            this.rightButton.Size = new System.Drawing.Size(62, 53);
            this.rightButton.TabIndex = 5;
            this.rightButton.Text = "RGHT";
            this.rightButton.UseVisualStyleBackColor = true;
            this.rightButton.MouseEnter += new System.EventHandler(this.rightButton_MouseHover);
            this.rightButton.MouseLeave += new System.EventHandler(this.rightButton_MouseLeave);
            // 
            // button1
            // 
            this.button1.Location = new System.Drawing.Point(87, 154);
            this.button1.Name = "button1";
            this.button1.Size = new System.Drawing.Size(61, 55);
            this.button1.TabIndex = 6;
            this.button1.Text = "slow";
            this.button1.UseVisualStyleBackColor = true;
            this.button1.Click += new System.EventHandler(this.button1_Click);
            // 
            // latency
            // 
            this.latency.Location = new System.Drawing.Point(13, 154);
            this.latency.Name = "latency";
            this.latency.Size = new System.Drawing.Size(68, 22);
            this.latency.TabIndex = 7;
            this.latency.Text = "FWD";
            // 
            // latency2
            // 
            this.latency2.Location = new System.Drawing.Point(13, 187);
            this.latency2.Name = "latency2";
            this.latency2.Size = new System.Drawing.Size(68, 22);
            this.latency2.TabIndex = 7;
            this.latency2.Text = "BCK";
            // 
            // Form1
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(8F, 16F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(357, 221);
            this.Controls.Add(this.latency2);
            this.Controls.Add(this.latency);
            this.Controls.Add(this.button1);
            this.Controls.Add(this.rightButton);
            this.Controls.Add(this.backButton);
            this.Controls.Add(this.leftButton);
            this.Controls.Add(this.forwardButton);
            this.Controls.Add(this.connectButton);
            this.Controls.Add(this.comboBox1);
            this.KeyPreview = true;
            this.Name = "Form1";
            this.Text = "Car Control";
            this.KeyDown += new System.Windows.Forms.KeyEventHandler(this.Form1_KeyDown);
            this.KeyUp += new System.Windows.Forms.KeyEventHandler(this.Form1_KeyUp);
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.ComboBox comboBox1;
        private System.Windows.Forms.Button connectButton;
        private System.Windows.Forms.Button forwardButton;
        private System.Windows.Forms.Button leftButton;
        private System.Windows.Forms.Button backButton;
        private System.Windows.Forms.Button rightButton;
        private System.Windows.Forms.Button button1;
        private System.Windows.Forms.TextBox latency;
        private System.Windows.Forms.TextBox latency2;
    }
}

